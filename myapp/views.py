from django.shortcuts import render, redirect
import os
from gtts import gTTS


# Create your views here.

def home(request):

    tts_content = request.GET.get('tts_content', '')
    if tts_content:
        gtts2 = gTTS(text=tts_content, lang = 'ko')
        gtts2.save("%s.mp3" % os.path.join('./TTS2/', "gtts2"))
        print("%s.mp3" % os.path.join('./TTS2/', "gtts2"))
        return redirect('home')
        
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')
