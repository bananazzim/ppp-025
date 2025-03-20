import math

r=int(input("원의 반지름을 입력해주세요=>"))

pi=math.pi

circle_circumference=2*r*pi

circle_area=r**2*pi

print(f"원주는 {circle_circumference:.1f}, 원의 면적은 {circle_area:.2f} 입니다.")