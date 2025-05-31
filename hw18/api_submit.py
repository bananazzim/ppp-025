# 강의자료 중 sfarm_hw.py의 submit_to_api() 함수 이용. 소수점 1자리까지 반올
# 림해서 제출
# 1) 전주시(146)의 2012년 연 강수량은?
# 2) 전주시(146)의 2024년 최대기온은? max of tmax
# 3) 전주시(146)의 2020년 최대 일교차(tmax-tmin)는?
# 4) 수원시(119)와 전주시(146)의 2019년 총강수량 차이는(절대값)? 


import requests
import os
import pandas as pd

def download_file(region, year):
    URL = f"https://api.taegon.kr/stations/{region}/?sy={year}&ey={year}&format=csv" 
    with open(f"hw18/weather_{region}_{year}_{year}.csv", "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)


def t_max_gap(t_max,t_min):
    max_gap = t_max[0] - t_min[0]
    for i in range(len(t_max)):
        gap = t_max[i] - t_min[i]
        if max_gap <= gap:
            max_gap = gap

    return max_gap
    
def submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=False):
    base_url = "http://sfarm.digitalag.kr:8800/submission/create"
    params = {
        "name": name,
        "affiliation": affiliation,
        "student_id": student_id,
        "param1": answer1,
        "param2": answer2,
        "param3": answer3,
        "param4": answer4,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        if verbose:
            print("응답 코드:", response.status_code)
            print("제출 성공! 응답:", response.text)
        return True
    except requests.exceptions.RequestException as e:
        if verbose:
            print("제출 중 오류 발생:", e)
        return False


def main():
    filename2012 = "hw18/weather_146_2012_2012.csv"
    if not os.path.exists(filename2012):
        download_file(146,2012)

    filename2024 = "hw18/weather_146_2024_2024.csv"
    if not os.path.exists(filename2024):
        download_file(146,2024)

    filename2020 = "hw18/weather_146_2020_2020.csv"
    if not os.path.exists(filename2020):
        download_file(146,2020)

    filename2019_suwon = "hw18/weather_119_2019_2019.csv"
    if not os.path.exists(filename2019_suwon):
        download_file(119,2019)

    filename2019_jeonju = "hw18/weather_146_2019_2019.csv"
    if not os.path.exists(filename2019_jeonju):
        download_file(146,2019)

    df_2012 = pd.read_csv("hw18/weather_146_2012_2012.csv", skipinitialspace=True)
    total_rainfalls = round(df_2012["rainfall"].sum(),1)
    print(total_rainfalls)       #1번답 1359.7 mm
    
    df_2024 = pd.read_csv("hw18/weather_146_2024_2024.csv", skipinitialspace= True)
    maxmax_t = round(df_2024["tmax"].max(),1)          #2번답 36.5℃
    print(maxmax_t)

    df_2020 = pd.read_csv("hw18/weather_146_2020_2020.csv", skipinitialspace= True)  
    max_t_gap = round(t_max_gap(df_2020["tmax"],df_2020["tmin"]),1)
    print(max_t_gap)
                                            #3번답 19.3℃

    df_2019_jeonju = pd.read_csv("hw18/weather_146_2019_2019.csv", skipinitialspace= True)
    df_2019_suwon = pd.read_csv("hw18/weather_119_2019_2019.csv", skipinitialspace= True)
    rainfall_gap = round(abs(df_2019_jeonju["rainfall"].sum()- df_2019_suwon["rainfall"].sum()),1)
    print(rainfall_gap)                          #4번답  49.0℃
    
    name = "조지형"
    affiliation = "스마트팜학과"
    student_id = "202217729"

    answer1 = total_rainfalls
    answer2 = maxmax_t
    answer3 = max_t_gap
    answer4 = rainfall_gap

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)
 



if __name__ == "__main__":
    main()