import os
import uuid
from pathlib import Path

from django.utils import timezone
from gtts import gTTS

from main.settings import BASE_DIR, MEDIA_URL ,MEDIA_ROOT
from rest_framework import serializers
from .models import TestToSpeech
from . import engine

class TestToSpeechSerializer(serializers.ModelSerializer):
    chapter_name = serializers.CharField(write_only=True)
    class Meta:
        model = TestToSpeech
        fields = ("novel_name", "chapter_name", "chapter_content","chapter_url")
        # fields = "__all__"
        read_only_fields = ("chapter_url",)
        extra_kwargs = {
            'chapter_name': {'write_only': True},
            'novel_name': {'write_only': True},
            'chapter_content': {'write_only': True},
        }


    def create(self, validated_data):
        # Get the text content from the uploaded file
        text_content = validated_data['chapter_content']
        # Specify the directory and file name for the audio file
        # directory = BASE_DIR / "media"
        # directory.mkdir(exist_ok=True)
        directory = Path(MEDIA_ROOT)
        directory.mkdir(parents=True, exist_ok=True)
        audio_file_name = f"{timezone.now().strftime('%Y%m%d%H%M%S')}.mp3"
        # audio_file_path = os.path.join(directory, audio_file_name)
        audio_file_path = os.path.join(MEDIA_ROOT, audio_file_name).replace("\\", "/")

        try:
            tts = gTTS(text_content)
            tts.save(audio_file_path)
            # with open(audio_file_path, "wb") as fh:
            #     fh.write(b'')
            # # Save text_content to audio_file_path using your desired method
            # engine.save_to_file(text_content, audio_file_path)
            # print(f"file saved {audio_file_path}")
            # engine.runAndWait()
            # Open the audio file and assign it to chapter_url
            with open(audio_file_path, 'rb') as audio_file:
                # validated_data["chapter_url"] = ContentFile(audio_file.read(), audio_file_path)
                validated_data["chapter_url"] = MEDIA_URL + audio_file_name
        except Exception as e:
            # Handle any errors during file generation or reading
            raise serializers.ValidationError("Failed to generate or read the audio file." + str(e))

        return super().create(validated_data)



