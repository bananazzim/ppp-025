import random


chosung_list  = [
    "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ",
    "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ",
    "ㅋ", "ㅌ", "ㅍ", "ㅎ"
]

def to_chosung_ch(ch):
    return chosung_list[(ord(ch) - ord('가'))// 588]


def to_chosung(text):
    full_text = []
    for ch in text:
        full_text.append(to_chosung_ch(ch))
    return full_text




def main():
    problems = ["바나나", "딸기", "토마토", "복숭아"]

    solution = problems[random.randrange(len(problems))]
   
    for i in range(3):
        
        answer = input(f"{to_chosung(solution)} =>")
        is_correct = False
       
        if answer == solution:
            print("정답입니다")
            is_correct = True
            break

        else:
            print("오답입니다.")

        if is_correct:
            print("잘하셨습니다.")

        else:
            print("게임오버. 다시 해보세요.")


if __name__ == "__main__":
    main()