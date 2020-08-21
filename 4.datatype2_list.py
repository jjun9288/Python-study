# dataType2
#  기본자료형 : int, float, str, bool

# ex) var변수에서 각 단어를 뽑아낸다.

var = "one two three four"
print(var.split())

# 1. list
#  여러 데이타를 묶어서 저장, 관리할 수 있는 자료형
#   -다른 타입의 데이타도 저장 가능
#     -> 각 요소는 인덱스( 0 ~ )를 사용하여 접근할 수 있다.

# 1) 리스트의 선언
#  변수 이름 = [data,data,data,...]

num1 = 100
str1 = "hello"
list1 = [1,2,"three",4,"five"]

print(type(num1))   #num1 상자에 담겨진 데이타의 타입은?  int
print(type(str1))   #str1 상자에 담겨진 데이타의 타입은?  str
print(type(list1))  #list1 상자에 담겨진 데이타의 타입은? list

# 2) 리스트의 인덱싱- 변수이름[index]

list1 = [1,2,"three",4,"five"]
print("0번째 데이타 : ",list1[0])
print("2번째 데이타 : ",list1[2])
print("-1번째 데이타 : ",list1[-1])

print(type(list1[2]))   #<class 'str'>
print(list1[2][0])      #t


# 3) 리스트의 슬라이싱
#  변수 이름[시작위치:끝위치] -> 시작위치 <=   < 끝위치

list1 = [1,2,"three",4,"five"]
print("0번째 부터 2번째 직전까지의 데이타 : ",list1[:2])
print("2번째부터 끝까지 : ",list1[2:])

#dataType1 (복제)

num1 = 100
num2 = num1
print("num1 : %d, num2 : %d" %(num1,num2))
print("num1의 주소 : ",id(num1))
print("num2의 주소 : ",id(num2))     #같은 주소가 나온다.

num2 = 200
print("num2의 주소 : ",id(num2))     #덮어씌워짐

str1 = "hello"
str2 = str1
str2 = str1[:3]
str2 = str1[:]     #이미 hello가 있어서 갖다 씀. 그래서 같은 주소가 나온다.
print("str1 : %s , str2 : %s" %(str1,str2))
print("str1의 주소 : ",id(str1))
print("str2의 주소 : ",id(str2))


#리스트 복제(복사)
#  주소값이 같으면 (list2 = list1) 깊은 복사
#  주소값이 다르면 (list2 = list1[:]) 얕은 복사

list1 = [1,2,"three",4,"five"]
list2=list1
print(list2)
list3=list1
print(list2)   #list2 list3는 같은 값일까? yes

print("list1의 주소 : ",id(list1))
print("list2의 주소 : ",id(list2))  #같은 주소가 나온다.

list2[0] = 'one'
print(list1)
print(list2)     #list1 list2 모두 1 이 one 으로 바뀐다.


list2=list1[:]
print(id(list1))
print(id(list2))   #list2와 list1은 다른 주소값이 나온다.

list2[0] = 'one'
print("list1의 데이타 : ",list1)
print("list2의 데이타 : ",list2)   #list2만 1이 one 으로 바뀐다.


# 4) 리스트의 연산
#  + : 리스트의 연결

data1 = ["one",2,3]
data2 = [4,5,"six",7]
data3 = data1 + data2
print(data3)   #['one',2,3,4,5,'six']

#  * : 리스트의 반복
data4 = data1 * 3
print(data4  #[] 안에 data1이 세번씩 반복


# 5) 리스트 관련 함수(메서드)
#  (1) list.append()  -> 추가

list1 = [1,2,"three",4,"five"]
list1.append("six")     #하나까지만 가능
print(list1)

list1.append([7,8,9,"ten"])  #리스트 안에 리스트 추가를 할 수 있다.
print(list1)


#  (2) list.extend()  -> 확장

list1 = [1,2,"three",4,"five"]
list1.extend([6,7,8,9,"ten"])
print(list1)      #[1, 2, 'three', 4, 'five', 6, 7, 8, 9, 'ten', 't', 'e', 'n']

#list1.extend("ten") -> [1, 2, 'three', 4, 'five', 6, 7, 8, 9, 'ten']
#list1.extend(100)   -> ERROR

#  (3) list.insert(index,요소)  -> 원하는 위치에 요소 추가

list1 = [1,2,"three",4,"five"]
list1.insert(0,"zero")
print(list1)
list1.insert(2,4)
print(list1)

#  (4) list.pop(index)  -> 원하는 위치의 요소 제거

list1.pop(1)
print(list1)
list1.pop()
print(list1)  # 마지막 데이타 제거


#  (5) list.remove(요소)  -> 원하는 요소 제거

list1.remove("three")
print(list1)
# list1.remove("one") -> 존재하지 않으면 ERROR 
list1.remove(4)
print(list1)  # -> 먼저 나오는 요소 제거


#  (6) list.index(요소)  -> 요소의 위치

print(list1.index(4))
# print(list1.index(1)) -> 존재하지 않으면 ERROR


#  (7) list.count(요소)  -> 요소의 갯수

print(list1.count(4))  # 4 라는 요소가 1개 있다.
print(list1.count(8))  # 0, ERROR 안 남


#[특정 요소의 포함여부]
#  요소 in 변수이름  -> True, False

print( 4 in list1)  # 4라는 요소가 list1에 있는가? True
print( 1 in list1)


#  (8) list.sort()  ->정렬

s1 = [3,6,1,23,75,23]
print(s1)
s1.sort()   #s1 상자에 담긴 실제 데이타를 정렬시켜줌!
print(s1)


#  (9) list.reverse()  -> 역순으로 정렬

s1 = [3,6,1,23,75,23]
s1.reverse()
print(s1)














