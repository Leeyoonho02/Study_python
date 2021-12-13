def sum(num) :

    if num == 1 :

        return num

    return num + sum(num-1)

num = int(input())

print(sum(num))