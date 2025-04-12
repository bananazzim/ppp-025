def read_db(filename):
    calorie_dic = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",") # => ["밀", "334","100"]
            calorie_dic[tokens[0]] = int(tokens[1])/int(tokens[2])

              #오른쪽꺼는 왼쪽에 쓴거에 들어간다

    return calorie_dic
  



def main():

    fruit_calories= read_db("hw09/calorie_db.csv")

    fruit_ate_G = {"밀":200 , "쑥갓":300}


    total=0
    for item in fruit_ate_G:
        total += (fruit_calories[item]* fruit_ate_G[item])

    print(f"총 칼로리는 {total} kcal 입니다.")
        
        
if __name__ == "__main__":
    main()