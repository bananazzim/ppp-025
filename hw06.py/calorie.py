def main():
    #한라봉 , 딸기 , 바나나

    fruit_calories={"한라봉":1,"딸기":0.34 , "바나나":0.77}

    fruit_eat={"한라봉":100,"딸기":100,"바나나":100}

    fruit_total=["한라봉","한라봉","딸기","바나나"]

    total=0
    
    for item in fruit_total:
        total = total+(fruit_eat[item]*fruit_calories[item])
        
    print(f"섭취한 과일의 총 칼로리는 {total} kcal 입니다")

if __name__ == "__main__":
     main()



#아 뭐야이거거
     
    
