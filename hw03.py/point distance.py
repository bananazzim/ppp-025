import math

x1=int(input("첫 번째 점의 x좌표를 입력해주세요=>"))

y1=int(input("첫 번째 점의 y좌표를 입력해주세요=>"))

x2=int(input("두 번째 점의 x좌표를 입력해주세요=>"))

y2=int(input("두 번째 점의 y좌표를 입력해주세요=>"))

distance=math.sqrt((x1-x2)**2 +(y1-y2)**2)

print(f"두 점 사이의 거리는 {distance:.2f} 입니다.")

