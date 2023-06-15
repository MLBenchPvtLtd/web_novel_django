from django.urls import path
from .views import TestToSpeechView
urlpatterns = [
    path('generate/', TestToSpeechView.as_view(), name='generate'),

]



