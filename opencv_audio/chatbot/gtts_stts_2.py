from gtts import gTTS
from playsound import playsound


file_name = "tts_ko_2.mp3"

# tts(Ko)
txt = "엄마와 누나야 강변살자."
tts_ko = gTTS(text=txt, lang="ko")
tts_ko.save(f"chatbot\resource\{file_name}")
playsound(r"chatbot\resource\tts_ko_2.mp3")
