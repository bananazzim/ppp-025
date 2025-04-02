
   

def total_calorie(fruits,fruits_calorie_dic):
 
    calorie_total=0
    
    for item in fruits:
        calorie_total += fruits[item]* fruits_calorie_dic[item]/100

    return calorie_total



def main():
    fruits={"딸기":300 , "한라봉":150}
    fruits_calorie_dic={"한라봉":50 , "딸기":34 , "바나나":77}
    print(f"섭취한 총 칼로리는 {total_calorie(fruits,fruits_calorie_dic)} 입니다.")


if __name__ == "__main__":
    main()