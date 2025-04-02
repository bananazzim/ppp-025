def average(nums):
    result = sum(nums) / len(nums)
    return result


def main():
    number_list= "3,5,6,7,3,26,28,11,15"
    nums = [int(nums) for nums in number_list.split(",")]
    print(f"받은 숫자들의 평균은 {average(nums):.2f} 입니다.")


if __name__ == "__main__":
    main()