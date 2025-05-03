# 과제 10를 2022년 자료가 아닌 2020년 자료를 이용하여 풀이하시오.
# 1) 연 평균 기온(일평균 기온의 연평균)
# 2) 5mm이상 강우일수
# 3) 총 강우량


import os
import requests

def download_weather(filename):

    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def readfile(filename,col_idx):
    weather_info = []
    with open(filename, encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_info.append(float(tokens[col_idx]))
            
    return weather_info

def year_avg_temp(avg_t):
    avg_temp = sum(avg_t)/len(avg_t)


    return avg_temp

def more_than_5mm(rain_ryang):
    days = 0 
   
    for i in rain_ryang:
        if i >= 5:
            days += 1

   

    return days

def total_rain(rain_ryang):
    total_r= sum(rain_ryang)

    return total_r






def main():
    filename = "hw12/weather_146_2020_2020.csv"
    if not os.path.exists(filename):
        download_weather(filename)
   
    avg_t = readfile(filename,4) 
    year_temp = year_avg_temp(avg_t)
    print(f"2020년의 연평균 기온은 {year_temp:.1f}℃ 입니다.")

    rain_ryang = readfile(filename,9)
    rain_days_more_than_5mm = more_than_5mm(rain_ryang)
    print(f"2020년의 5mm 이상 강우일수는 {rain_days_more_than_5mm}일 입니다.")

    total_rainfall = total_rain(rain_ryang)
    print(f"2020년의 총 강우량은 {total_rainfall}mm 입니다.")
   
    
   



if __name__ == "__main__":
    main()

