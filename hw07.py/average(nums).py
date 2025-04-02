def average(nums):
    result = sum(nums) / len(nums)
    return result


def main():
    number_list= [3,5,6,7,3,26,28,11,15]

    print(f"받은 숫자들의 평균은 {average(number_list)} 입니다.")


if __name__ == "__main__":
    main()