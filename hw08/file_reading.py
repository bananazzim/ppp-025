# def text2list(input_text):
#     text_list = input_text.split()        쪼개줬잖아
#     nums=[]                                  리스트로 처리해줬잖아 다해줬잖아 
#     nums = [int(nums) for nums in text_list]  이건 대체 왜 안되는거야야 제발발

def text2list(txt):
    txt_list = txt.split()
    nums = []                                           
    for num_text in txt_list:                           
        nums.append(int(num_text))
    return nums




def read_text(filename):
    text = ""
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print(f"!{line.strip()}!")
            text += " "+ line.strip()
    return text

def numbers_gatsu(numnumber):

    return len(numnumber)

def numbers_average(numnumnumber):
    return sum(numnumnumber)/len(numnumnumber)

def max(numnumnumnumber):
    max_num = numnumnumnumber[0]

    for num in numnumnumnumber:

        if max_num < num:
            max_num= num

    return max_num

def min(numnumnumnumnumber):
    min_num = numnumnumnumnumber[0]

    for num in numnumnumnumnumber:

        if min_num > num:
            min_num= num

    return min_num

def median(numnumnumnumnumnumnumber):

    sorted_list = sorted(numnumnumnumnumnumnumber)


    return sorted_list[len(sorted_list)//2]






def main():
    text= read_text("hw08/numbers.txt")
    nums_list = text2list(text)

    print(f"총 숫자의 개수는 {numbers_gatsu(nums_list)}개 입니다.")

    print(f"주어진 숫자의 평균은 {numbers_average(nums_list):.0f}입니다.")

    print(f"주어진 숫자의 최댓값은 {max(nums_list)}입니다.")

    print(f"주어진 숫자의 최솟값은 {min(nums_list)}입니다.")

    print(f"주어진 숫자의 중앙값은 {median(nums_list)}입니다. ")



    

   

    


if __name__ == "__main__":
     main()