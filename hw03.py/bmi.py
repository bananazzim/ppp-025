import math

weight=int(input("몸무게를 입력해주세요=>"))

height=int(input("키를 입력해주세요=>"))

height_m= height/100

bmi=weight/math.pow(height_m,2)

print(f"BMI는 {bmi:.1f} kg/m**2 입니다.")