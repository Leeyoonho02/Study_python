#정수 2개 입력, 합/평균 출력

a, b, c = map(int,input().split())

d = sum([a, b, c])/3

print(a + b + c , format(d,".2f"))