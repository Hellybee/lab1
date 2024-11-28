# 마이크 음성 인식
import speech_recognition as sr

# 마이크로 음성 입력
recog = sr.Recognizer()
with sr.Microphone() as source:
    print("1초 후에 말하세요.")
    audio = recog.listen(source)
try:
    # 구글 API로 인식 (API Key가 없으면 하루에 50회만 사용 가능)
    txt = recog.recognize_google(audio, language="ko")
    # txt = recog.recognize_google(audio, language='en-US')
    print(txt)
except sr.UnknownValueError:
    print("음성인식 실패")
except sr.RequestError:
    print("요청 실패: {}".format(100))
