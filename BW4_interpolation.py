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
value = 1.234

old_way = '%-10s = %.2f' % (key, value)

new_way = '%(key)-10s = %(value).2f' %{
    'key' : key,'value' : value # 원래방식
}

reordered = '%(key)-10s = %(value).2f' %{
    'value' : value, 'key' : key # 바꾼 방식
}

# 전혀 문제없이 돌아간다!
assert old_way == new_way == reordered

# 첫번째 문제점인, tuple 내 데이터의 값의 순서를 바꾸거나 값의 타입을 바꿔도 된다!

name = '철수'
template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요'

before = template % (name, name) # 튜플

template = '%(name)s는 음식을 좋아해. %(name)s가 요리하는 모습을 봐요'
after = template % {'name' : name}

assert before == after
# 같은 키를 지정할 수 있어서 같은 값을 반복하지 않아도 되므로, 
# 세번째 문제점인, 튜플에서 같은 값을 계속 반복하지 않아도 된다. 
#  template % {'name' : name}

# 하지만 딕셔너리를 사용하면, 또 다른 문제점이 발생하는데, 
## 4. 바로 시각적 잡음이 많아진다는 것이다.

for i, (item, count) in enumerate(pantry):
    before = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))

    # 형식화 식에 딕셔너리를 사용하니 엄청 번잡스러워졌음..
    # 이것이 바로 네번째 문제점!
    after = '#%(loop)d: %(item)-10s = %(count)d' % {
        'loop' : i + 1,
        'item' : item.title(),
        'count' : round(count),
    }
    
    assert before == after
  

# 지금 각 key를 최소 두번(한번은 형식 지정자, 한번은 딕셔너리 key에) 반복한다. 
# 변수를 세번, 네번까지 써야할 상황이 존재할 수 있음


soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup' : soup}
print(formatted)

# 딕셔너리 원소가 많아질수록, 
# 형식화 문자열이 많아질수록, 
# 계속 형식화 문자열과, 딕셔너리를 위아래로 훑어보면서 뭐가 뭔지 뒤져야함..

## 따라서 더 나은 방법이 있어야한다!

## 파이썬 3 부터는 %를 사용하는 오래된 c 스타일 형식화 문자열 보다, 더 표현력이 좋은 '고급 문자열 형식화' 기능이 존재!

a = 1234.5678
# 소수점 두 자리까지 표시하고 천 단위로 쉼표를 추가하여, 부동 소수점 숫자 a를 형식화
formatted = format(a, ',.2f')
print(formatted)

b = 'my 문자열'
# 이는 문자열 b를 너비가 20인 필드 내에서 가운데 정렬
formatted = format(b, '^20s')
print ('*', formatted, '*')

# %d와 같은 c스타일 형식화 지정자를 사용하는 대신, 위치 지정자 {}를 사용할 수 있다.

key = 'my_var'
value = 1.234

# 위치 지정자는 format 메서드에 전달된 인자 중 '순서상' 같은 위치에 있는 인자를 가르킨다.
formatted = '{} = {}'.format(key, value)
print(formatted)

# 각 위치 지정자에는 콜론 뒤에 형식 지정자를 붙여넣어 문자열에 값을 넣을때,
# 어떤 형식으로 변환할지 정할 수 있다.

# '<' 는 왼쪽 정렬을 의미하며
# 10은 필드의 폭을 나타냅니다. 
# ':' 이후의 부분은 값이 삽입될 위치
formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted) 

# 파이썬은 '%'나 '{}'를 출력하려면 두번쓰면됨.
print('%.2f%%' % 12.5)
# 1.23은 앞의 위치지정자에 들어감
print('{} replaces {{}}'.format(1.23))

# Key, vlaue의 인덱스를 위치 지정자에 줄 수 있다.
# 그러면 자유롭게 위치 변환이 가능하다.

formatted = '{1} = {0}'.format(key,value)
print(formatted)

# 이를 여러번 사용할 수 있다.

name = '영우'
name2 = '소영'
# 소영은 format(인덱스0, 인덱스1) 에서 인덱스1에 위치해있기에 '소영'이 먼저나옴!
formatted ='{1}은 음식을 좋아해. {0}이 요리하는 모습을 봐요.'.format(name, name2)
print(formatted)

# 하지만 여전히 문자열이 길어질수록, 딕셔너리 키가 많아 질수록 가독성이 떨어짐.
# 그래서 format()을 사용하는 법은 알아야하되, 사용은 자제하자.

## 그래서 파이썬 3.6부터는 '인터폴레이션'을 통한 형식 문자열.
## 짧게 'f-문자열'이 등장했다!

key = 'my_var'
value = 1.234

formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

## {key!r:<10} : repr() 함수 예시
# {key} : 이 부분은 f-string 내에서 변수 key를 문자열로 삽입합니다.
# !r: 이 부분은 f-string 내에서 repr() 함수를 사용하여 변수를 "문자열로 표현"합니다. 
# repr() 함수는 변수의 공식적인 문자열 표현을 반환합니다. 
# 예를 들어, 문자열에 따옴표를 붙여서 문자열이나 객체를 나타내거나, 특수 문자를 이스케이핑하는 등의 작업을 수행합니다.
# :<10 : 이 부분은 10자리 너비 내에서 왼쪽 정렬을 의미합니다. 
# 만약 key의 문자열 표현이 10자리를 초과하면 잘리게 됩니다. << 이건 몰랐네?
key = "example"
formatted = f'{key!r:<10}'
print(formatted)

## 자 이제 진짜 얼마나 짧아졌는지 보자.

