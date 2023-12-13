# 형식화(formatting)은 미리 정의된 문자열에 데이터 값을 끼워 넣어서 사람이 보기 좋은 문자열로 저장하는 과정.
# 파이썬에는 총 4가지 방식으로 형식화 가능
# 나중에 설명할 1가지 방법 외에는 모두 치명적인 단점 존재!

# 1. 가장 일반적인 방법은 '%' 연산자를 사용하는 것.
# 이를 '형식 문자열' 이라고 부른다.

a = 0b1011011
b = 0xc5f

print('이진수: %d, 십육진수 : %d' % (a, b))

# 이는 C의 printf에서 비롯됐으며, 파이썬에 이식됬다.
# %s, %x, %f 등 많이 지원한다.
# 파이썬을 처음 사용하는 사람들은 이게 익숙해서 이렇게 자주 사용함..
# but, 4가지의 문제점 존대.

## C formatting의 단점
## 1. tuple 내 데이터의 값의 순서를 바꾸거나 값의 타입을 바꾸면 타입변환이 불가능하므로 오류발생

# 일단 얘는 잘 작동함.
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

# but key와 value의 위치를 바꾸면 실행 시점에 예외가 발생하는데,
key2 = 'my_var2'
value2 = 1.2345
#formatted2 = '%-10s = %.2f' % (value2, key2)
# TypeError: must be real number, not str
# print(formatted2)

# 마찬가지로, 오른쪽 파라미터의 순서를 그대로 유지하고, 형식 문자열의 순서를 바꿔도 오류가남.
key3 = 'my_var2'
value3 = 1.2345
#formatted3 = '%.2f = %-10s' % (key3, value3)
# TypeError: must be real number, not str
# print(formatted3)

# 이런 오류를 피하려면 % 연산자의 좌우가 서로 잘 맞는지 계속 검사해야함!
# 코드를  변경할떄마다 사람이 직접 검사해야하므로, 검사과정에서 실수하기 쉬움


## 2. 포매팅을 하기 전에 값을 살짝 변경해야한다면,(이런경우 많음) 식을 읽기가 매우 어려워진다는 것.

# pantry 튜플 선언.
pantry = [
    ('abocado', 1.25),
    ('banana', 2.5),
    ('cherry', 15)
]

for i, (item, count) in enumerate(pantry):
    # '%d' : 정수 
    # '%-10s' : 0자리 왼쪽 정렬된 문자열
    # ' %.2f' : 소수점 둘째자리까지의 부동소수점 숫자
    print('#%d: %-10s = %.2f' % (i, item, count))

    
# 이제 여기서 값을 조금 바꿔서 출력된 메세지를 좀 더 쓸모있게 보고싶을때 문제 발생

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        # index를 1부터 시작하기 위해 i + 1 
        i + 1,
        # 품목의 이름을 대문자로 시작하는 형태로 변환.
        # abocado -> Abocado
        item.title(),
        # 소수점 이하를 반올림하여 정수로 변환.
        round(count)
    ))

# 생각보다 가독성이 너무 나빠진다. 

## 3. 형식화 문자열에서 같은 값을 여러번 사용하고 싶다면, 튜플에서 같은 값을 여러번 반복해야함.
template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요.'
name = '철수'
formatted = template % (name, name)
print(formatted)

# 이런식으로 같은 값을 계속 반복해야 한다면, 값을 살짝 변경해야하는 경우 실수하기 쉽고
# 코딩하기에도 성가시다. 

# 아래 예시처럼, 어느 한군데에는 title() 메서드 호출을 잊어버릴 수 있다..
name = 'youngwoo'
formatted = template % (name.title(), name)
print(formatted)

# 이런 문제점을 해결하기 위해 파이썬의 % 연산자에는 튜플 대신 딕셔너리를 사용해 형식화하는 기능이 추가됬음
# 딕셔너리의 키는 형식 지정자에 있는 키(예 : %(key)s)와 매치됨.

key = 'my_var'
value = 