def average(nums):
    return sum(nums) / len(nums)

def get_weather_data(filename,col_idx):
    weather_datas=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens= line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas



def count_bigger_days(nums,criteria):
    
    basket = []
    for num in nums:
        if num >= criteria:
            basket.append(num)

    return len(basket)

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
    print(events)
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

def sumifs(rainfalls, months, selected=[6,7,8]):
    # for rain in rains: 랑 똑같은 의미
    total = 0
    for i in range(len(rainfalls)):#리스트의 길이를 구해서 반복해보는거임 c 언어 스타일인데 이렇게 해야 months를 뽑을수 있어서 이렇게함
         rain= rainfalls[i]
         month = months[i]
         if month in selected:
             
             total += rain

    return total

def main():
    filename = "lecture10/weather_146_2022-2022.csv"
    
    tavgs = get_weather_data(filename, 4)
    # 1. 일평균 기온의 연평균 
    print(f"연 평균 기온(avg. of 일평균)은은  {average(tavgs):.2f} ℃")

    # 2. 5mm 이상인 강우일수
    rainfalls = get_weather_data(filename, 9)
    count_over5rain = count_bigger_days(rainfalls , 5)
    # count_over5rain = len([x for x in rainfalls >= 5])
    print(f"5mm 이상 강우일수 = {count_over5rain}일")

    # 3. 총 강수량은 
    print(f"총 강수량은 = {sum(rainfalls)} mm")

    # 4. 최장연속 강우일수
    print(f"최장연속 강우일수는 = {max(get_rain_events(rainfalls))}일")

    # 5. 강우이벤트 중 최대 강수량은? get_rain_events 에서 일수를 더하는게 아닌
    #강수를 더해버리면 해결이 됨

    # 6. top3 of tmax
    top3_tmax =sorted(get_weather_data(filename, 3), reverse=True)[:3]
    top3_tmax =sorted(get_weather_data(filename, 3))[-3:]  #둘다가능
    print(f"가장 높았던 최고기온 3개는 {top3_tmax}입니다.")

    # 7. 여름철(6월~8월) 총 강수량
    #rainfalls는 이미 위에서 읽었음음
    months = get_weather_data_int(filename, 1) #왜 int로 바꾸셨지?
    print(f"여름철 총 강수량은 {sumifs(rainfalls,months,selected=[6,7,8]):.1f} 입니다.")

    # 8. 2021년과 2022년의 총 강수량을 구하시오

    filename_20yr = "lecture10/weather(146)_2001-2022.csv"
    

if __name__=="__main__":
    main()
