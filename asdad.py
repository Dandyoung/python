
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

