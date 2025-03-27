t_c=int(input("섭씨 몇도를 변환할지 입력해주세요=>"))


def c2f(t_c):
    tem_F=(t_c * 9/5) + 32
    
    print(f"{t_c}℃ => {tem_F}℉")
    return ""

print(c2f(t_c))   
    
if __name__ == "__c2f__":
    c2f()