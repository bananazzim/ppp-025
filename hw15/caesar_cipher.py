
def caesar_encode_ch(ch,shift):
    return chr(ord(ch) + shift)
    
def caesar_encode(text:str , shift: int =3):
    full_text = []
    
    for ch in text:
        encoded_ch = caesar_encode_ch(ch,shift)
        full_text.append(encoded_ch)

    return "".join(full_text)             #리스트를 빈칸으로 합쳐주기

def caesar_decode( text: str, shift:int=3):
    return caesar_encode(text, -shift)

def main():

    print(caesar_encode(input("넣을 문자를 입력해주세요=>")))

    print(caesar_decode(input("넣을 문자를 입력해주세요=>")))



if __name__ == "__main__":
    main()