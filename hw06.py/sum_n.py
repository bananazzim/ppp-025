n=int(input("1부터 몇까지 합을 구할까요?=>"))


def sum_n(n):

    total=0
    for i in range(n):
        x=i+1
        total += x

    return total


print(sum_n(n))

if __name__ == "__sum_n__":
    sum_n()
