# [자료형] int : 정수, float : 실수, str(string) : 문자열

# [조건문] if elif else

# [연산자] += -= /= 등.. **:거듭제곱

# [나눗셈] //:나눗셈 몫, %:나눗셈 나머지.

# [비교연산자] <, >, <=, >=, ==(같다), !=(다르다)

# [불(bool)] 0이면 true, 아니면 false. not, and, or 가능

# [비트단위 연산자] ~(not), &(and), |(or), ^(xor),

# [비트시프트 연산] a<<b = a*(2^b), a>>b = a*(2^-b)

# [split] a, b = input().split(":") # split 안에 있는것 기준으로 나눈다. # "" 는 공문자.

# [sep] print(a, b, sep=":") # sep= 에 있는 것으로 둘을 구분해 출력.

# [3항 연산] c = (a if (a>=b) else b) if가 true면 a, false면 b

# [문자열 반복] print(a*int(b)) # 문자열*정수(정수*문자열) = 정수만큼 문자열 반복

# [소수점 반올림] format(a/b,".nf") # 소수점 n번째 자리에서 반올림

# [유니코드] ord() : 유니코드문자 > 정수, chr() : 반대

# [for 반복문] for i in range(10) : # range(시작, 끝, 증감)

# [print end] print에 end="" 넣으면 줄바꿈 대신 해당문자 출력. / 문자열 사이 +하면 공백없이 붙음

# [format] print("{}x{}={}".format(i,j,a)) : {} 자리에 순서대로 i j a 들어간다.

# [f-string] print(f"{i}+{j}={a}")

# [% 서식문자] s = 'my age %d' %a : a가 %d에 들어간다. 자료형 구분 필요.

# [% 서식문자 자료형 구분] %s 문자열, %d 정수, %f 실수 / %o,x 각각 8, 16진수 문자열로 변환

# [ a[n] ] n-1번째 문자. split로 나뉘어져 있다면 n-1번째 덩어리.

# [진수변환] int(~~,n진수) : ~~(n진수) 를 10진수로 변환

# [반복실행 중] break : 반복실행 중단. continue : 이번 반복 건너뛰기