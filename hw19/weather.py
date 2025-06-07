import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib



def download_weather(station_id, year, year2, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year2}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "utf-8"
        f.write(resp.text)

def main():
    filename="weather_146_1980_2024.csv"
    download_weather(146, 1980, 2024, filename)

    df=pd.read_csv(filename, skipinitialspace=True)
    winter = df[df["month"].isin([12, 1, 2])]
    summer = df[df["month"].isin([6, 7, 8])]
    plt.hist(winter["tavg"].dropna(), color='blue')
    plt.hist(summer["tavg"].dropna(), color='red')
    plt.xlabel("평균온도(파랑=겨울, 빨강=여름)")
    plt.ylabel("해당 온도 포함 날짜 수")
    plt.savefig("./data_1980_2024_tem_w_s.png")

    birth_month=3
    birth_day=11

    selected = df[(df["month"] == birth_month) & (df["day"] == birth_day)]
    plt.figure(figsize=(30, 6))
    plt.xticks(ticks=range(1980, 2025, 1))
    plt.plot(selected["year"], selected["tavg"], color="blue")
    plt.xlabel("년")
    plt.ylabel("평균 온도")
    plt.savefig("./birth_1980_2024")

    after_birth = selected[selected["year"] >= 2002]

    birth_after_max_tem=after_birth["tavg"].max()
    birth_after_min_tem=after_birth["tavg"].min()
    birth_1980_2024_max_tem=selected["tavg"].max()

    birth_after_max_tem_year = after_birth[after_birth["tavg"] == birth_after_max_tem]["year"].values[0]
    birth_after_min_tem_year = after_birth[after_birth["tavg"] == birth_after_min_tem]["year"].values[0]
    birth_1980_2024_max_tem_year = selected[selected["tavg"] == birth_1980_2024_max_tem]["year"].values[0]
    

    print(f"2002년도 이후 가장 더웠던 6월 4일의 연도는{birth_after_max_tem_year}년, 기온은 {birth_after_max_tem}이며 가장 추웠던 연도는{birth_after_min_tem_year}년, 기온은{birth_after_min_tem}입니다.")
    print(f"1980년 이후 가장 더웠던 6월 4일의 연도는{birth_1980_2024_max_tem_year}년, 기온은 {birth_1980_2024_max_tem}입니다.")


    fig, ax=plt.subplots()
    df["date"]=pd.to_datetime(df[["year","month","day"]])

    df.plot("date","tavg", ax=ax)
    plt.savefig("hw19/data_1980_2024")
   
if __name__=="__main__":
    main()