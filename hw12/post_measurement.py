#코드를 이용하여, 2020년 전주 측후소 주소를 다운로드 받아서, 저장하시오.


import requests
    
URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
with open("hw12/weather_146_2020_2020.csv", "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)