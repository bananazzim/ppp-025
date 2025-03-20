x=int(input("x의 좌표를 입력해주세요=>"))

y=int(input("y의 좌표를 입력해주세요=>"))

if x>0 and y>0:
    print("입력하신 좌표는 제1사분면입니다.")

elif x<0 and y>0:
    print("입력하신 좌표는 제2사분면입니다.")

elif x<0 and y<0:
    print("입력하신 좌표는 제3사분면입니다.")

elif x>0 and y<0:
    print("입력하신 좌표는 제4사분면입니다.")

else: print("입력하신 좌표는 영점입니다.")           