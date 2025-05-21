import random


def gugudan():
    first_number = random.randint(1,9)
    second_number = random.randint(1,9)
    try:
        answer = int(input(f"{first_number} X {second_number} = ?"))

    except ValueError:
        print(f"오답입니다.")
        return False
    
    if answer == first_number * second_number:
        print(f"정답입니다.")
        return True
    
    else :
        print(f"오답입니다.")
        return False

    

def main():
    score = 0
    how_many = int(input(f"몇 문제 도전하시겠습니까? =>"))
    for i in range(how_many):
        is_correct = gugudan()
        if is_correct:
            score += 1
    print(f"{how_many}문제 중 {score}문제를 맞춰 {score*100/how_many}점 입니다 고생하셨습니다.")



if __name__ == "__main__":
    main()