# 1-45 숫자 중 중복이 되지 않게 6개를 추출하여 보여주기.
# 사용자가 원하는 횟수를 입력하면, 해당횟수만큼 반복해서 번호 추출하기

import random

def lotto(how_many):
    lotto_number = []

    while True:  
        number = int(random.randrange(1,45))
        if number not in lotto_number:
            lotto_number.append(number)
        
        
        if len(lotto_number) == how_many:
            break


        
    return lotto_number
def main():
    try:
        how_many = int(input(f"몇 회만큼 번호를 추출하실래요?=>"))
    except ValueError:
        print("자연수를 입력해주세요.")
    print(f"행운의 숫자는 {lotto(how_many)}입니다.")



    


if __name__ == "__main__":
    main()