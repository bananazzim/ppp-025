size=int(input("얼마나 큰 삼각형을 그릴지 수를 넣어주세요=>"))

for i in range(size):
    n=i+1
    star="*"
    empty_space=""
    print(f"{n*star}")