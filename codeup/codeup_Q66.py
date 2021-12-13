# 정수 3개 받아 홀짝 구분하기

a, b, c = map(int,input().split())

if a%2 == 0 :
    print("even")

else :
    print("odd")

if b%2 == 0 :
    print("even")

else :
    print("odd")

if c%2 == 0 :
    print("even")

else :
    print("odd")


# 반복문으로 간단하게 할 수 있지 않을까?

a, b, c = map(int,input().split())

list = [a, b, c]

for i in list :

    if i%2 == 0 :
        print("even")

    else :
        print("odd")

