import speech_recognition as sr
from gtts import gTTS
import playsound
from bs4 import BeautifulSoup as bs
import requests
import json
import re

r = sr.Recognizer()
# 마이크로 음성 입력
with sr.Microphone() as source:
    print("1초 후에 말하세요.")
    audio = r.listen(source)
try:
    # 구글 API로 인식 (API Key가 없으면 하루에 50회만 사용 가능)
    txt = r.recognize_google(audio, language="ko")
    # txt = recog.recognize_google(audio, language='en-US')
    print(txt)
except sr.UnknownValueError:
    print("음성인식 실패")
except sr.RequestError:
    print("요청 실패: {}".format(100))


neighborhood = "서울"
api_key = f"{neighborhood}+날씨"
url_ = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="

api_ = url_ + api_key

html = requests.get(api_)

print(html.status_code)
soup = bs(html.text, "html.parser")

data1 = soup.find("div", {"class": "status_wrap"})  # 특정 태그 값을 가져온다.
json_data = ""

if data1:
    print("Data found:", data1.prettify())  # 보기 좋게 출력

    # 원하는 정보를 JSON으로 변환 (예: 텍스트 내용 추출)
    weather_info = data1.get_text(strip=False)
    data_dict = {"weather_info": weather_info}  # 가공된 텍스트
    json_data = json.dumps(data_dict, ensure_ascii=False, indent=4)

else:
    print("날씨 정보를 찾을 수 없습니다.")

print("--------------------------------------------------")
text = re.split(":", json_data)[1]  # str타입으로 출력 | 필요없는부분 제거
# text = re.split("     CCTV 날씨지도 초단기예측 ", text)[0]

# print(text)
# file = sr.AudioFile('')
# text = "안녕하세욤~ 파이썬으로 노는 것은 재미있습니다."

tts = gTTS(text=text, lang="ko")

tts.save("today_weather.mp3")  # 오디오 저장


playsound.playsound("./today_weather.mp3")  # 저장한 오디오 재생
