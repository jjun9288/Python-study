#inputFunction
# I/O Function
# - OutputFunction
#      print()
# - InputFunction
#      input()

print("----START----")
input()
print("----End----")


print("----START----")
input("숫자를 입력하세요: ")
print("----End----")


print("----START----")
num1 = input("숫자를 입력하세요: ")
num1 = int(num1)
#num1 = int(num1)
#num1 = int(input("숫자를 입력하세요 : "))  -> 이 두 가지 경우에는 데이타 타입 int
print("사용자가 입력한 데이터 : ", num1)
print(type(num1))   #-> 출력되는 모든 데이타 타입은 str!

print("----End----")

#ex) 입력받은 숫자의 제곱을 출력하고자 한다면
#print(num1*num1)  ERROR
#print(num1**2)    ERROR num1은 str이므로!!

#[형변환]
#  int(data) -> data를 정수로 변환하여 반환
#  float(data) -> data를 실수로 반환하여 반환
#  str(data) -> data를 문자열로 변환하여 반환

print("----START----")
num1 = input("숫자를 입력하세요: ")
num1 = int(num1)
print(num1*num1)
print("----End----")


#[여러개의 값을 동시에 입력받기]
#  input() + split() = input().split()
#    -> 입력 받은 문자열.split() = list로 반환
#    -> 입력 받은 문자열을 구분자 기준으로 잘라내어 list로 반환한다.
#        (구분자가 없으면 공백을 기준으로 잘라낸다)

l1 = input("문자열을 입력하세요 : ").split()   #['문자열을', '입력하세요', ':'] 
print(l1)
l1 = input("두 개의 정수를 입력하세요 : ").split()
print(l1)
l1 = input("두 개의 정수를 입력하세요 : ").split(",")
print(l1)

#  map()  -> 여러개의 데이타를 한번에 형변환
#   map(자료형,LIST)
#      --> LIST의 데이타를 해당 자료형으로 형변환하여 list로 반환
l1 = input("두 개의 정수를 입력하세요 : ").split(",")
a,b = map(int,l1)
print(a,b)

                                      
                                      



      
