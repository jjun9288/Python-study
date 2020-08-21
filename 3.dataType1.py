#연산자
#  산술연산자 : + , - , * , / , %(나머지)
#  대입연산자 : =(우항을 좌항에 대입),
#  ->연산자에도 우선순위가 있다. () > ... > 대입연산자(=)
#  관계연산자 : <, <=, >, >=, ==, !=
#  -> 좌항과 우항 관계를 확인하여 True or False 논리결과 알려줌
#  논리연산자 : and, or, not
#    and : 좌항과 우항 모두 True 여야 True 반환, 나머지는 False
#    or  : 좌항과 우항이 모두 False 여야 False 반환, 나머지는 True
#    not : 우항만 존재, 우항의 값을 반전하여 반환


num1 = 100
num2 = 200
result1 = num1 + num2
print("result1 : %d"%(result1))
result2 = num1 * num2
print("result2 : %d"%(result2))
result3 = num1 % num2
print("result3 : %d"%(result3))


num1 = "100"
num2 = "200"
result1 = num1 + num2
print("result1 : ",result1) #문자열은 연산 불가, num1 + num2 = 100200
print(type(result1)) #<class 'str'>


#DataType1 (자료형)
#기본자료형 : bool, int, float, str
#  1.숫자 자료형 : int(정수), float(실수)  -> 100:정수, 100.0:실수
#   ex)0o34(8진수), 0x2A(16진수) 또한 int

i1 = 100
i2 = 200
r1 = 100.0
r2 = 200.0

print(type(i1), type(r1))   #<class 'int'> <class 'float'>


#숫자형 데이타의 연산
#  (1) 사칙연산 : + , - , * , /
#     -> 정수와 정수 나눗셈은 실수가 나올 수 있다.
#

result1 = i1 + i2
print("result1 = ",result1)  #300
result2 = r1 + r2
print("result2 = ",result2)  #300.0

result1 = i1 /i2
print("result1 = ",result1)  #0.5
print(type(result1))  # <class 'float'> !!
result2 = r1 / r2
print("result2 = ",result2)  #0.5


#  (2) 몫(//)과 나머지(%)

x1 = 100
x2 = 23
y1 = 100.0
y2 = 23.0
result1 = x1 % x2
print("result1 = ", result1)
result2 = x1 % x2
print("result2 = ", result2)
result1 = y1 // y2
print("result1 = ", result1)  #4
result2 = y1 // y2
print("result2 = ", result2)  #4.0


#  (3) 거듭제곱(**)  ->Python에서만 가능, 다른 언어에서는 함수를 만들어야 함.

a1 = 3
a2 = 4
result1=a1**a2
print("result1 = ", result1)


#[생각더하기]

i1=130
i2=3
#ex) i1을 i2로 나누었을 때의 값을 출력하고자 한다면 -> /
print("i1 / i2 = ", i1 / i2)
print("i1 / i2 = %f" %(i1 / i2))  
#ex) i1을 i2로 나누었을 때의 몫을 출력하고자 한다면 -> //
print("i1 // i2 = ", i1 // i2)
print("i1 // i2 = %d" %(i1 // i2))
print("i1 // i2 = %d" %(i1 / i2))   #43
#ex) i1을 i2로 나누었을 때의 나머지를  출력하고자 한다면 -> %
print("i1 % i2 = ", i1 % i2)
#print("i1 % i2 = %d" %(i1 %i2))  #에러 남 (%가 문자열로 인식이 안 된다.)
print("i1 %% i2 = %d" %(i1%i1))  # 출력되면 i1%%i2로 나와야 되는거 아닌가요?

# * "%0.4f" %3.41312245
#   >>>3.4131 (소숫점 4째 자리까지만 출력)

#  2. 문자열 자료형 : str
#   -> " , '
#   -> """, ''' 개행이 포함된 문자열

print("hello\nworld")
str1 = '''hello
world'''          #== str1 = hello\nworld
print(str1)      # -> 보기 불편해서 개행문자(\n) 사용하는걸 추천한다.


#문장열 연산자
str1 = "hello"
str2 = "world"

# (1) 문자열 연결 (+) , 좌항과 우항의 타입이 다르면 ERROR
print(str1 + str2)

# (2) 문자열 반복 (*)
print(str1*3)

# (3) 문자열 인덱싱과 슬라이싱
#   문자열 인덱싱
#      변수 이름[index]
#        ->번호는 1이 아닌 0부터 센다.
#        ->마이너스(-) 기호를 이용하면 마지막 값부터 읽는다. (-1부터)

py = "Life is too short"
print(py[0])      #L
print("py 문자열의 5번째 값 : ",py[5])
print("py 문자열의 -1번째 값 : ",py[-1])  #t

#   문자열 인덱싱
#      변수이름[시작위치:끝위치]
#        시작위치 <=   < 끝위치
print("py문자열의 2번째부터 10번째 전까지의 문자열 : ",py[2:10])
print("py문자열의 3번째부터 끝까지의 문자열 : ",py[3:])   #뒤 숫자를 안 쓰면 됨
print("py문자열의 처음부터 10번째 전까지의 문자열 : ",py[:10])  #앞 숫자를 안 쓰면 됨
print("py문자열의 3번째부터 -1까지의 문자열 : ",py[3:-1])


#[생각더하기]
# py = "life is too short"
# py 문자열의 값을 Life is Too short"로 변경 (8번재 값 t 를 T로 변경)
# py[8] = 'T'   ->index로 접근하여 문자열의 값을 변겅할 수는 없다!

print(py[:8] + 'T' + py[9:])

py= py[:8] + 'T'+ py[9:]
print(py)


# (4) 문자열 관련 함수
#   {1} 변수이름.count("문자")  -> 변수에서 해당 문자의 갯수로 변환

py='Life is too short'
print("py변수 데이타의 i문자의 갯수 : ",py.count("i"))
print("py변수 데이타의 2번째부터 i문자의 갯수 : ",py.count('i',2))


#   {2} 변수이름.find("문자") -> 변수에서 해당 문자를 찾아 그 위치(index) 변환
#   {3} 변수이름.index("문자") == 변수이름.find("문자")

py='Life is too short'
print("py에서 o 문자의 위치 : ", py.find("o"))
print("py에서 o 문자의 위치 : ", py.index("o"))   #9
print("py에서 o 문자의 위치 : ", py.find("o",11))   #14
#find 와 index의 차이점
print("py에서 a 문자의 위치 : ", py.find("a"))   #해당 문자가 존재하지 않으면 -1 반환
print("py에서 a 문자의 위치 : ", py.index("a"))  #해당 문자가 존재하지 않으면 ERROR


#   {4} 변수이름.replace("문자","문자") (or "문자열","문자열")
#    ->해당 변수의 데이타에서 문자1을 문자2로 (문자열1 에서 문자열2로) 치환하여 변환

py='Life is too short'
print("py에서 is를 ffff로 치환 : ", py.replace("is","ffff"))

#   {5} 변수이름.split("구분자")
#    ->해당 변수의 데이타를 구분자 기준으로 잘라내어 list로 변환
#         구분자를 지정하지 않으면 공백을 기준으로 자른다!

py='Life is too short'
print("py변수의 데이타를 자르면? : ", py.split())


# 3. 논리자료형 (bool 자료형)
#      True, False 의 데이타 저장
#  관계연산자 : <, <=, >, >=, ==, !=
#  -> 좌항과 우항 관계를 확인하여 True or False 논리결과 알려줌
#  논리연산자 : and, or, not
#    and : 좌항과 우항 모두 True 여야 True 반환, 나머지는 False
#    or  : 좌항과 우항이 모두 False 여야 False 반환, 나머지는 True
#    not : 우항만 존재, 우항의 값을 반전하여 반환

num1 = 100
num2 = 34
print("num1 > num2 : ", num1>num2)
result1 = num1 > num2
print("result1 : ", result1)
print(type(result1))   #<class 'bool'>

print("num2는 0보다 작거나, 100보다 큽니까? : ", num2 < 0 or num2 > 100)
print("num2는 0보다 크고 100보다 작습니까? : ", num2 > 0 and num2 < 100)




#[과제]
#num = 세자리 숫자가 주어질 때, 일의 자리, 십의 자리, 백의 자리를 각각 출력하시오.

num=435
num1=num // 100
num2=num % 100 // 10
num3=num % 100 % 10 // 1
print("일의 자리 : %d" %num3)
print("십의 자리 : %d" %num2)
print("백의 자리 : %d" %num1)


#-> 출력결과
# 일의 자리 : 5
# 십의 자리 : 3
# 백의 자리 : 4