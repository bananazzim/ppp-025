



def is_leap_year(y):
    if y%4 ==0 and y%100 != 0 :
        print(f"{y}년은 윤년입니다.")

    elif y%4 == 0 and y%100 == 0 :
        print(f"{y}년은 윤년이 아닙니다.")

    else :
        print(f"{y}년은 윤년이 아닙니다. ")

    return ""


def main():
    x= int(input("몇 년인지 입력해주세요=>"))
    print(is_leap_year(x))



if __name__ == "__main__":
    main()