from rest_framework import generics, response, status
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser

from .models import (
    TestToSpeech
)
from .serializers import (
    TestToSpeechSerializer
)


# Create your views here.

class TestToSpeechView(generics.GenericAPIView):
    queryset = TestToSpeech.objects.all()
    serializer_class = TestToSpeechSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return response.Response(serialized.data, status=status.HTTP_201_CREATED)
        return response.Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
