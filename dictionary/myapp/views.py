from django.shortcuts import render, redirect
import os
from gtts import gTTS


# Create your views here.

def home(request):
    return render(request, 'home.html')

def tts(request):
    if request.method == "POST":
        text = request.POST.get('text')
        gtts = gTTS(text = text, lang='ko')
        gtts.save("%s.mp3" % os.path.join('./TTS/', "gtts"))
        print("%s.mp3" % os.path.join('./TTS/', "gtts"))
        return redirect('tts')
    return render(request, 'tts.html')
