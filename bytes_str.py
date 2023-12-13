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

