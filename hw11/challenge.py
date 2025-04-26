#3. 2001년부터 2022년까지 각 해마다 4월부터 시작해서, 적산온도가 200이 넘는
#최초일을 구하시오

def readfile(filename,col_idx):
    weather_data =[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_data.append(float(tokens[col_idx]))

    return weather_data

def weather_dates(filename):
    weather_dates= []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]),int(tokens[1]),int(tokens[2])])

    return weather_dates

def cal_gdd(years,tavg,dates):
    base_temp = 5
    total_gdd = 0
    for i in range(len(tavg)):
        t = tavg[i]
        year = dates[i][0]   
        if dates[i][1] in [4,5,6,7,8,9,10,11,12]:
            if year == years:
                if t >= 5:
                    total_gdd += t-base_temp

                elif t < 5:
                    t-base_temp == 0

                    if total_gdd >= 200:
                        return dates[i]
   

 


def main():
    filename = "hw11/weather146_2001_2022.csv"
    dates = weather_dates(filename)
    tavg = readfile(filename,4)
    years = 2000

    for i in range(1,23):
        years += 1
        gdd = cal_gdd(years,tavg,dates)
        print(f"{years}년의 적산온도가 200℃을 넘긴 최초일은 {gdd[0]}년 {gdd[1]}월 {gdd[2]}일 입니다.")

if __name__ == "__main__":
    main()
