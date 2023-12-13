# 레파지토리 연동 안될때
# https://stackoverflow.com/questions/59790948/cant-push-refs-to-remote-try-running-pull-first-to-integrate-your-changes

# PEP 8 스타일(아래가이드)를 따른다면,
# 1. 파이썬 커뮤니티와 공통된 스타일을 공유하면, 협업시 도움이 됨
# 2. 일관성있는 스타일을 사용하면, 자신이 작성한 코드를 쉽게 수정 가능


# import문은 한줄에 하나씩.
import numpy
import sys

# 이렇게 쓰는 것은 괜찮음
from numpy import square, sign

# 와일드카드 import는 최대한 피해야함! 아래처럼 작성하지 말기. 혼란을 야기함
from numpy import *



# 이렇게 수직정렬해서 쓰거나
foo = function_name(var_one, var_two,
                    var_three, var_four)

# 이렇게 쓰기
foo = funciton_name2(
    var_one, var_two,
    var_three, var_four)


# 탭 보다는 공백(4칸)을 들여쓰기 방법으로 사용하기.
# 참고로 Python3부터는 탭과 공백의 혼합을 허용 x (에러로 간주)

# 연산자의 앞에서 들여쓰기 하기!
income = (gro_ss 
          + asd 
          + dadsad
          + (div - abbb)
          - asdaa)

# 공백을 추가하는것을 피해야하는 상황

# 1. (), {}, [] 바로 안쪽
# Wrong
[ 1, 2, lst[ 3 ] ]
# Correct
[1, 2, lst[3]]

# 2. 쉽표와 그 뒤에 오는 닫는괄호 사이
# Wrong
t = (1, )
# Correct
t = (1,)

# 3. 쉽표, 세미콜론, 콜론 바로 앞
# Wrong
if x == 3 :
  return x , y
# Correct
if x == 3:
  return x, y

# 4. 함수 호출 시 인자 목록을 시작하는 여는 괄호 앞
# Wrong
func (100)
# Correct
func(100)

# 5. 인덱싱이나 슬라이싱을 하는 여는 괄호 바로 앞
# Wrong
dct ['key'] = lst [index]
 
# Correct
dct['key'] = lst[index]

# 6. 연산자끼리 정렬하기 위해 여러개의 공백을 사용
# Wrong
x             = 1
y             = 2
long_variable = 3
 
# Correct
x = 1
y = 2
long_variable = 3

## 우선 순위가 다른 연산자들을 사용하는 경우, 우선순위가 낮은 연산자 주위에 공백을 사용해야 한다.
## 연산자의 양쪽에 같은 개수의 공백을 사용해야 한다.

# Wrong
i=i+1
total +=1
x = x * 2 - 1
result = x * x + y * y
c = (a + b) * (a - b)
 
# Correct
i = i + 1
total += 1
x = x*2 - 1
result = x*x + y*y
c = (a+b) * (a-b)

