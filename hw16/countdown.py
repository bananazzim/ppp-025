import time


def countdown(number):

    for n in range(number):
        print(f"{(number-n)}...", end="\r")
        time.sleep(1)

    print(f"시간이 끝났습니다.")

def main():
    countdown(int(input("숫자를 넣어주세요=>")))

if __name__ == "__main__":
    main()