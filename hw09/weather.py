#기상자료를 받아서 연 평균 기온(일평균 기온의 연평균), 5mm이상 강우일수, 총 강우량을 구하시오.


def average_temps(date_rows,temp_index):
    total_temp=0
    total_days=0

    for row in date_rows:
        total_temp += float(row[temp_index])
        total_days += 1

        return total_temp/total_days
    

def rain_info(date_rows,rain_index):
    rainy_days = 0
    total_rain_yang = 0

    for row in date_rows:
        rain_yang = float(row[rain_index])
        total_rain_yang += rain_yang

        if rain_yang >= 5:
            rainy_days += 1

    return rainy_days,total_rain_yang


def main():
    
    # 파일을 불러오고고
    filename = 'hw09/weather_146_2022_2022.csv'
        #열어서 정리를 하는데 어떻게 장대한 파일에서 딱 해당하는 열만 쏙 가져올까?
    with open(filename, 'r', encoding='utf-8-sig') as file:
        all_data = [line.strip().split(', ') for line in file]

        #아 분명 이부분이 문제인데
    title = ['year','month','day','tmax', 'tavg','tmin','humid','wind','sunshine','rainfall']
    data_rows = all_data[1:]
            #리스트에서 쏙 그 해당하는 열만 빼와야하는데
    temp_index = title.index('tavg')
    rain_index = title.index('rainfall')

    avg_temp=average_temps(data_rows,temp_index)
    rainy_days,total_rain = rain_info(data_rows,rain_index)

    print(f"연평균 기온은 {avg_temp:.1f}℃ 입니다.")
    print(f"5mm 이상 강우일수는 {rainy_days}일 입니다.")
    print(f"총 강우량은 {total_rain:.1f} mm 입니다.")

    #아 제발 왜이래래

   

if __name__ == "__main__":
    main()
  



        

  
