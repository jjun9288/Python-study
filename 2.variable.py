#변수 (variable)
#데이터를 저장하기 위해 프로그램에 의해 이름을 할당받은 메모리 공간

#변수이름 = 데이터
#<변수 이름 규칙>
# 1. 절대적 규칙
#   - 문자,숫자,_만 사용 가능
#   (첫번째 글자가 숫자면 안 된다.)
#   - 예약어를 이름으로 사용 불가능
#   (if, while, for, and, or, ...)
# 2. 암묵적 규칙
#   - 첫번째 글자는 소문자로 작성
#   (클래스 이름은 첫번재 글자를 대문자로 지정)
#   - 두 단어가 연결되는 경우에는 연결되는 부분의 첫번째 글자를 대문자로 지정
#   ex) boxSize, box_size

box1 = 100 #box1이라는 상자에 100이라는 변수
box2 = '100' #box2라는 상자에 100이라는 정수


print(box1)
print(box2)
print('box1: ',box1)
print('box2: ',box2)

box1 = 1000
box2 ='hello world'
print('box1: ',box1)
print('box2: ',box2)


name ='윤준영'   #문자열
age = 25         #정수
height = 184.7   #실수

print("name : %s, age : %d, height : %.1f" %(name,age,height))


#type(변수이름)
#  -> 변수가 담고 있는 데이터의 타입을 알려준다.

name ='윤준영'   #문자열
age = 25         #정수
height = 184.7   #실수

print(type(name))    #<class 'str'>
print(type(age))     #<class 'int'>
print(type(height))  #<class 'float'>


#파이썬 예약어
#   -> True : 참, False : 거짓

data_type = True
print(type(data_type))  #<class 'bool'>


#id(변수이름)
#  -> 해당 변수의 메모리 주소값을 알려준다.

name='윤준영'
print(id(name))  #57706776










