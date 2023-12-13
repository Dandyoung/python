# 파이썬에는 문자열 데이터의 시퀀스를 표현하는 두가지 타입이 있다.
# 바로 bytes와 str 이다. 

# bytes type의 인스턴스에는 부호가 없는 8비트 데이터가 그대로 들어간다.
a = b'h\x65llo'

print(list(a))
print(a)

# str 인스턴스에는 사람이 사용하는 언어의 문자를 표현하는 유니코드 '코드포인터'가 들어있다.

a = 'a\u0300 propos'

print(list(a))
print(a)

# 여기서 중요한 사실은 str 인스턴스에는 직접 대응하는 이진 인코딩이 없고
# bytes에는 직접 대응하는 텍스트 인코딩이 없다는 점이다.

# 유니코드 데이터를 이진 데이터로 변환하려면,
# str 은 encode 메서드 호출
# bytes는 decode 메서드 호출

# 일반적으로는 UTF-8이 시스템 디폴트 인코딩 방식임

# to_str : bytes나 str 인스턴스를 받아서 항상 str을 반환하는 함수
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # str 인스턴스

# 이 줄은 바이트열 b'foo'을 to_str 함수에 전달하여 변환한 후, 그 결과를 출력합니다. 
# 바이트열은 UTF-8 인코딩을 사용하여 문자열로 디코딩됩니다. 
# 따라서 출력 결과는 단순히 문자열 'foo'가 됩니다.
print(repr(to_str(b'foo')))
#: 이 줄은 문자열 'bar'을 to_str 함수에 전달하여 변환한 후, 그 결과를 출력합니다. 
# 하지만 to_str 함수 내에서 문자열에 대한 변환은 수행되지 않고, 입력값 그대로 반환됩니다.
print(repr(to_str('bar')))
print(repr(to_str(b'\xed\x95\x9c')))

# to_bytes : bytes나 str 인스턴스를 받아서 항상 bytes를 반환하는 함수
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # bytes 인스턴스


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글')))

## 꼭 기억해야할 것!
## 1. bytes와 str이 똑같이 작동하는 것처럼 보이지만, 각각의 인스턴스는 서로 호환되지 않음
## 그래서, 전달중인 문자 시퀀스가 어떤 타입인지를 항상 잘 알고 있어야 함!

#'+' 연산자를 사용하면 bytes를 bytes에 더하거나 str을 str에 더할 수 있다!#
print(b'one' + b'two')
print('one' + 'two')
# but, bytes 와 str을 더할 순 없다. 아래 코드 돌리면 에러뜸
# can only concatenate str (not "bytes") to str
# print('one' + b'two')

# 똑같이 bytes는 bytes끼리, str은 str끼리만 비교할 수 있다.

# ASCII에서 'r'은 'b'보다 큰 값이므로 이 비교는 참.
assert b'red' > b'blue'
# 유니코드에서 'r'이 'b'보다 큰 값이므로 이 비교도 참
assert 'red' > 'blue'

## assert 문이 뭘까?
## 디버깅과 테스트를 위해 주로 사용된다. 특정 조건이 참인지 여부를 확인하는데 사용.

# 두 번째 인자 b가 0일 때 assert 문을 사용하여 예외적인 상황을 처리합니다. 
# 만약 b가 0이라면 "Cannot divide by zero"라는 메시지를 출력하고 프로그램을 중단.
def divide(a, b):
    assert b != 0, "0으로 나눌 수 없습니다."
    return a / b

result = divide(10, 2)
print(result)  # Output: 5.0

# Uncomment the following line to see an AssertionError
# result2 = divide(10, 0)

# assert 문은 가정이 충족되지 않으면 프로그램 실행을 중단함.
# 엄청 powerful한 코드이다. 따라서 디버깅이나 테스트 중에만 활성화 되야하고 프로덕션 코드에서는 비활성화되야한다.
# '-O'(optimize) 옵션을 사용하여 Python 인터프리터를 실행하면 assert 문이 무시되도록 할 수 있습니다.
# python -O bytes_str.py 처럼 쓰면 되는데,
# 근데 해당 상황에서는 어짜피 zeroDivisionError가 뜸 ㅎㅎ
 
 
# 다시 돌아와서 내부에 똑같은 문자열이 들어있더라도, bytes와 str 인스턴스가 같은지 비교하면
# 항상 false가 나온다.
print(b'foo' == 'foo')

# % 연산자는 각 타입의 형식화 문자열(format string)에 대해 작동한다.
# % 연산자는 문자열 포매팅.

# 이 줄은 바이트열 서식 문자열을 사용하여 바이트열을 생성합니다. 
# %s는 서식 지정자로, 여기에 해당하는 값이 b'blue'로 대체됨.
print(b'red %s' % b'blue')
# 이 줄은 문자열 서식 문자열을 사용하여 문자열을 생성합니다. 
# 여기서도 %s는 서식 지정자이고, 'blue'가 이에 해당하는 값으로 대체됨.
print('red %s' % 'blue')

# 하지만 파이썬이 어떤 이진 텍스트 인코딩을 사용할지 알 수 없으므로, str 인스턴스를 
# bytes 형식화 문자열에 넘길 수는 없다!
# print(b'red %s' % 'blue') << 에러뜸

# 근데, str에 bytes를 넘길수는 있지만, 이상하게 작동함
print('red %s' % b'blue')

# 이진 데이터를 파일에서 읽거나 파일에 쓰고 싶으면,
# 항상 이진모드('rb', 'wb')로 파일을 열어라!

# 유니코드 데이터를 파일에서 읽거나 파일에 쓰고 싶을떄는 시스템 디폴트 인코딩에 주의
# 인코딩 차이로 놀라고 싶지 않으면, open에 encodeing 파라미터를 명시적으로 전달!
# with open('data.bin', 'r', encoding='cp1252') as f:
#     data = f.read()
    
# assert data == 'noooo' 참고로 읽어온 데이터가 noooo가 아니라면, assert 문으로 인해, 프로그램이 중단됨!

