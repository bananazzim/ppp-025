
def get_range_list(n):
    numbers=[]

    for i in range(1,n+1):
        numbers.append(i)
    
    return numbers
  



def main():
    x=int(input("n을 입력해주세요=>"))
    print(get_range_list(x))
 
 

 
if  __name__ == "__main__":
    main()