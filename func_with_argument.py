import func as f

def mult(num1, num2, num3) : # 임자 있는 함수 (대부분)

    return num1 * num2 * num3

f.welcome()

print("Insert 3 number")

num1, num2, num3 = map(int,input().split()) # 반복되는 두 줄을 한줄로.

while num1 != 0 or num2 != 0 or num3 != 0 :

    print("Multi of {}, {}, {} is {}.".format(num1, num2, num3, mult(num1, num2, num3)))

    print("Insert 3 number")

    num1, num2, num3 = map(int,input().split())

print("Bye.")