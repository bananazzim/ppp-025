
def get_weather_data(filename,col_idx):
    weather_datas=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens= line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas


def get_rain_events(rainfalls):
    events = []
    continued_rain_days = 0
    for rain in rainfalls:
        if rain > 0:
            continued_rain_days += 1
        else:
            if continued_rain_days > 0:
                    events.append(continued_rain_days)
            continued_rain_days = 0 
    if continued_rain_days > 0:
        events.append(continued_rain_days)
    return events

def max_rainfalls(rainfalls):
    events = []
    total_rain = 0
    for rain in rainfalls:
        if rain > 0:
            total_rain += rain
        else:
            if total_rain > 0:
                    events.append(total_rain)
            total_rain = 0 
    if total_rain > 0:
        events.append(total_rain)

    return events

def get_weather_data_int(filename,col_idx):
    weather_datas=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens= line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(int(tokens[col_idx]))

    return weather_datas

def sumifs(rainfalls,months,selected=[6,7,8]):
    total = 0
    for i in range(len(rainfalls)):#리스트의 길이를 구해서 반복해보는거임 c 언어 스타일인데 이렇게 해야 months를 뽑을수 있어서 이렇게함
         rain= rainfalls[i]
         month = months[i]
         if month in selected:
             
             total += rain

    return total

def sumifs_2(rainfalls,years,selected=[2021,2022]):
    total = 0
    for i in range(len(rainfalls)):
         rain= rainfalls[i]
         year = years[i]
         if year in selected:
             
             total += rain

    return total

    
def main():


    filename = "hw10/weather_146_2022_2022.csv"
    # 최장연속 강우일수
    print(f"최장연속 강우일수는 {max(get_rain_events(get_weather_data(filename,9)))}일 입니다.")
    
    # 강우이벤트 중 최대강수량
    print(f"최대 강수량은 {max(max_rainfalls(get_weather_data(filename,9))):.1f}mm 입니다.")

    #가장 더운날 top3
    t_max = sorted(get_weather_data(filename,3))[-3:]
    print(f"가장 더운 날 top3의 온도는 {t_max}℃ 입니다.")

    #. 여름철(6월~8월) 총 강수량
    rainfalls = get_weather_data(filename,9)
    months = get_weather_data_int(filename, 1) #왜 int로 바꾸셨지?
    print(f"여름철 총 강수량은 {sumifs(rainfalls,months,selected=[6,7,8]):.1f} mm 입니다.")

    #2021년과 2022년 총 강수량
    filename_2001_2022 = "hw10/weather_146__2001_2022.csv"
    rainfalls = get_weather_data(filename_2001_2022,9)
    years = get_weather_data_int(filename_2001_2022, 0)

    print(f"2021-2022년 총 강수량은 {sumifs_2(rainfalls,years,selected=[2021,2022]):.1f} mm 입니다.")
if __name__ == "__main__":
    main()