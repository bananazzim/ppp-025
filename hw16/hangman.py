# 답=apple
# _ _ _ _ _ (trial=7) 답을 입력하시오 => a
# a _ _ _ _ (trial=7) 답을 입력하시오 => b
# 틀렸습니다.
# a _ _ _ _ (trial=6) 답을 입력하시오 => p
# a p p _ _ (trial=6) 답을 입력하시오 =>
# 다 맞추거나, trial=0이 되면 게임 종료

import random

def hangman(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
       

        if solution[i] == input_ch:
            answer[i] = solution[i]
            is_correct = True

    return is_correct



def main():
    problem = ["grape", "house", "report"]

    solution = problem[random.randrange(len(problem))]
    is_correct = False
    lives = 5

    answer = ["_" for n in range(len(solution)) ]
    print(answer)
    

    while True:
        
        input_ch = input(f"{''.join(answer)}? => _안에 무슨 글자가 들어갈까요?") 

        if hangman(solution, answer, input_ch):
                print(f"{input_ch}가 들어있습니다.")

        else:
            lives += -1
            

        if lives <= 0 :
            print(f"기회 소진되었습니다. 정답은 {solution} 였습니다.")

            break

        if "_" not in answer:
            print(f"정답은 {solution}! 잘하셨습니다. 게임 종료")
            break

        elif  input_ch not in solution:
            
            print("오답입니다. 다시 해보세요.")


if __name__ == "__main__":
    main()


