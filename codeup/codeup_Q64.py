# 세 정수 중 최솟값 출력

a, b, c = map(int,input().split())

d = (a if a<b else b) if ((a if a<b else b)<c) else c

print(int(d))
