weight=int(input("몸무게를 입력해주세요=>"))

height=int(input("키를 입력해주세요=>"))

height_m=height/100

bmi=weight/(height_m**2)

print(f"BMI는 {bmi} kg/m**2 입니다.")

if 23<= bmi <= 24.9:
    print("비만 전단계 입니다.")

elif 25<= bmi <= 29.9:
    print("1단계 비만입니다.")

elif 30<= bmi <= 34.9:
    print("2단계 비만입니다.")

elif 35<= bmi:
    print('3단계 비만입니다')           