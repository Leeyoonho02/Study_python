def fac(num) :

    if num == 1 :

        return num

    return fac(num-1)*num

num = int(input())

print(fac(num))