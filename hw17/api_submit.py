# 강의자료 중 sfarm_hw.py의 submit_to_api() 함수 이용. 소수점 1자리까지 반올
# 림해서 제출
# 1) 전주시(146)의 2015년 연 강수량은?
# 2) 전주시(146)의 2022년 최대기온은? max of tavg
# 3) 전주시(146)의 2024년 최대 일교차(tmax-tmin)는?
# 4) 수원시(119)와 전주시(146)의 2024년 총강수량 차이는(절대값)? 

import rich

import requests
import os

def download_file(region, year):
    URL = f"https://api.taegon.kr/stations/{region}/?sy={year}&ey={year}&format=csv" 
    with open(f"hw16/weather_{region}_{year}_{year}.csv", "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def readfile(filename,col_idx):
    weather_datas=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens= line.split(",")
            try:
            # print(tokens[col_idx], type(tokens[col_idx]))
                weather_datas.append(float(tokens[col_idx]))
            except (ValueError ,IndexError):
                continue
    return weather_datas

def sum_rain(rainfall):
    return sum(rainfall)

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
            success = "제출 성공!"
            rich.print(f"[bold magenta]{success}[/bold magenta]:grinning:", response.text)
        return True
    except requests.exceptions.RequestException as e:
        if verbose:
            fail = "제출 중 오류 발생"
            print(f"[bold magenta]{fail}[bold magenta]:angry:", e)
        return False
# rich.print(f" [bold magenta]{name}[/bold magenta]님 반갑습니다.:vampire:")
    


def main():
    filename2015 = "hw16/weather_146_2015_2015.csv"
    if not os.path.exists(filename2015):
        download_file(146,2015)

    filename2022 = "hw16/weather_146_2022_2022.csv"
    if not os.path.exists(filename2022):
        download_file(146,2022)

    filename2024 = "hw16/weather_146_2024_2024.csv"
    if not os.path.exists(filename2024):
        download_file(146,2024)

    filename2024_suwon = "hw16/weather_119_2024_2024.csv"
    if not os.path.exists(filename2024_suwon):
        download_file(119,2024)

    rainfall = readfile(filename2015,9 )
    total_rainfalls = f"{round(sum_rain(rainfall),1)}"         #1번답 813.5 mm
    
    t_avg = readfile(filename2022,4)
    t_avg_max = f"{round(max(t_avg),1)}"                        #2번답 30.5℃

    t_max,t_min = readfile(filename2024,3), readfile(filename2024,5)
    t_max_g = f"{round(t_max_gap(t_max,t_min),1)}"                #3번답 18℃

    suwon_rainfall = readfile(filename2024_suwon,9)
    jeonjoo_rainfall = readfile(filename2024, 9)
    suwon_total_rainfall = sum(suwon_rainfall)
    jeonjoo_total_rainfall = sum(jeonjoo_rainfall)
    gap = f"{round(abs(suwon_total_rainfall - jeonjoo_total_rainfall),1)} " #4번답 
    
    name = "조지형"
    affiliation = "스마트팜학과"
    student_id = "202217729"

    answer1 = total_rainfalls
    answer2 = t_avg_max
    answer3 = t_max_g
    answer4 = gap

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)
 



if __name__ == "__main__":
    main()