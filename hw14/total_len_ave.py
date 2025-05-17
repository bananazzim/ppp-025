# 숫자를 입력 받아서 그 리스트를 출력하시오.
# 숫자는 정수만 입력 받고, 자연수가 아닌 입력 값은 무시하시오.
# -1를 입력하면 입력을 더 이상받지 않고 현재까지 입력 받은 값을 출력하시오.
# 또한 총 개수와 평균을 구하시오

def listlist(numbers):
    number_list = []
    num = numbers.split(",")
    
    

    return num

def average(numbers):
    return sum(numbers)/len(numbers)

def get_nature(numbers):
    num_list = []
    for num in numbers:

        if int(num) == -1 :
            break
        else:
            try:
            
                if int(num) > 0:
                    num_list.append(int(num))

            except ValueError:
                print(f"자연수가 아닙니다.")

    return num_list
            

    


def main():
    numbers = input("넣을 숫자를 입력해주세요(ex:3,4,5)=>")
    real_number = listlist(numbers)

    result = get_nature(real_number)
    print(f"{len(result)}개의 자연수가 있고 평균은 {average(result)}입니다.")



if __name__ == "__main__":
    main()