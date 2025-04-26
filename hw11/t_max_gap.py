#1. 해당기간동안 연도별로 최대일교차가 발생한 일자와 일교차를 표시하시오

def readfile(filename,col_idx):
    weather_datas = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def get_weather_date(filename):
    weather_dates=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens= line.split(",")
        
            weather_dates.append([int(tokens[0]),int(tokens[1]),int(tokens[2])]) #[2001 2 23]

    return weather_dates


def t_max_gap(dates,t_max,t_min,years):

    max_gap_date =dates[0]
    max_gap =t_max[0]-t_min[0]

    for i in range(len(dates)):
        date = dates[i]
        temp_max = t_max[i]
        temp_min = t_min[i]
        gap = temp_max - temp_min
        year = date[0] #와 이거때문에 시간 1시간잡아먹었네
        if year == years:

            if max_gap < gap:
                max_gap = gap
                max_gap_date = date


    return [max_gap_date,max_gap]
   




def main():
    filename = "hw11/weather146_2001_2022.csv"
    dates = get_weather_date(filename)
    t_max = readfile(filename,3)
    t_min = readfile(filename,5)
    
    years = 2000

    for i in range(1,23):
        years += 1
        max_gap_date,max_gap = t_max_gap(dates, t_max , t_min , years)

        print(f"최대 일교차가 발생한 일자는 {max_gap_date[0]}년 {max_gap_date[1]}월 {max_gap_date[2]}일이고 일교차는 {max_gap:.1f}℃ 입니다. ")

    

if __name__ == "__main__":
    main()