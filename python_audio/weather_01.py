from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import json
import re

neighborhood = "서울"
api_key = f"{neighborhood}+날씨"
url_ = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="

api_ = url_ + api_key

html = requests.get(api_)

print(html.status_code)
soup = bs(html.text, "html.parser")

data1 = soup.find("div", {"class": "status_wrap"})  # 특정 태그 값을 가져온다.
json_data = ""
# pprint(data1)
# # print(data1)

if data1:
    print("Data found:", data1.prettify())  # 보기 좋게 출력

    # 원하는 정보를 JSON으로 변환 (예: 텍스트 내용 추출)
    weather_info = data1.get_text(strip=False)

    # formatted_weather_info = weather_info
    # 예시: 특정 문자를 추가하여 가공 (여기서는 "|" 구분자를 추가)
    # formatted_weather_info = (
    #     weather_info.replace("온도", "| 온도")
    #     .replace("비체감", "| 비체감")
    #     .replace("습도", "| 습도")
    # )
    # data_dict = {"weather_info": formatted_weather_info}  # 가공된 텍스트

    data_dict = {"weather_info": weather_info}  # 가공된 텍스트
    json_data = json.dumps(data_dict, ensure_ascii=False, indent=4)

else:
    print("날씨 정보를 찾을 수 없습니다.")


print("--------------------------------------------------")
print((json_data))
format_txt = re.split(":", json_data)[1]  # str타입으로 출력 | 필요없는부분 제거

print("--------------------------------------------------")
print(format_txt)
