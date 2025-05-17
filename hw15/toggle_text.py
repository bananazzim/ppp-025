# 1) ASCII 코드를 이용하여 입력받은 문자열을 대문자는 소문자로, 소문자는 대문
# 자로 바꾸시오.

def toggle_text(text:str):
    asc = ord(text)

    if 65<= asc <=90 :
       result =  asc +32
    
    elif 97 <= asc <= 122:
        result = asc -32

    return chr(result)

def main():

    print(toggle_text(input("알파벳 대문자 혹은 소문자를 입력해주세요 =>")))


if __name__ == "__main__":
    main()