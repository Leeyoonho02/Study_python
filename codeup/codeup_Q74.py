a = ord(input())

b = ord("a")

while a>=b :
    print(chr(b), end=" ") # print에 end="" 넣으면 줄바꿈 대신 해당문자 출력.
    b += 1