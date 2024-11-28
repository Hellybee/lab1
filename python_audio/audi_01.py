import speech_recognition as sr
from gtts import gTTS
import playsound

r = sr.Recognizer()

# file = sr.AudioFile('')
text = "안녕하세욤~ 파이썬으로 노는 것은 재미있습니다."

tts = gTTS(text=text, lang="ko")

tts.save("hello01.mp3")


playsound.playsound("./hello01.mp3")
