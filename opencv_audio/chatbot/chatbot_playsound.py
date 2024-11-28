# STT (Speech-to-Text): 음성을 문자로 변환해주는 툴
# TTS (Text-to-Speech): 문자를 음성으로 변환해주는 툴

from gtts import gTTS


# tts (en)

txt = "I want joke"
file_name = "tts_en_01.mp3"
tts_en = gTTS(text=txt, lang="en")
tts_en.save(r"chatbot\resource\{file_name}")


# mp3 재생
from playsound import playsound

playsound(r"chatbot\resource\tts_en_01.mp3")
