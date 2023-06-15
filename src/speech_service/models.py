from django.db import models
from model_utils.models import TimeStampedModel
from utils.file_utils import upload_user_media


# Create your models here.
class TestToSpeech(TimeStampedModel):
    novel_name = models.CharField(max_length=100)
    chapter_name = models.FileField(upload_to=upload_user_media)
    chapter_content = models.TextField()
    chapter_url = models.CharField(max_length=100)

    def __str__(self):
        return self.novel_name
