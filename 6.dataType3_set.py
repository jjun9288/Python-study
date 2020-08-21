# dataType3
# <복습> -논리 자료형 : bool
#        -숫자 자료형 : int, float
#        -시퀀스 자료형 : 가변 시퀀스 자료형 : list
#                      : 불변 시퀀스 자료형 : str, tuple, range 
# 1. Set(집합)
#   - 수학에서 나오는 집합과 같은 개념!
#   - 각 요소에 순서를 메길 수 없으며, 중복된 데이타를 갖지 않는다.
#  1) set의 선언
#    변수 이름 = {data, data, ...}

s1 = {1,2,3,2,"hello","hello","python"}
print(s1)
print(type(s1))     #<class 'set'>

#  2) set의 연산

s2 = {2,3,4,5,6,7,8}
s3 = {2,4,8,100.200}

#    & 교집합
print(s2 & s3)
#    | 합집합 (shift+\)
print(s2 | s3)
#    - 차집합
print(s2 - s3)

#  3) set 관련 메서드
# set.add()

print("s1 : ",s1)
s1.add(4)
print("s1 : ",s1)   #중복된 데이타는 추가 안 됨

#set.update()

s1 = {1,2,3,2,"hello","hello","python"}
s1.update([100])
print(s1)
s1.update([10,50,80])
print(s1)                      #add는 하나의 요소, update는 여러 개의 요소 추가
#set.remove()
s1.remove(2)
#s1.remove(5)     #ERROR
#set.discard()
s1.discard(1000)  #ERROR 나지 않음
#set.pop()  -> 임의의 요소를 가져와 반환한 후 삭제함
print("뽑힌 요소 : ",s1.pop())   #->임의의 요소 뽑기
print(s1)
#set.clear()

#[특정 요소 포함 여부]
# 요소 in 변수 이름 -> True, False

print(100 in s2)  #False
print(100 in s3)  #True

#ex) s2의 데이터를 하나씩 차례대로 출력
# [set의 인덱싱]
# --> 리스트 or 튜플로 변환

s1 = {3,5,6,"hello"}
l1 = list(s1)
t1 = tuple(s1)
print("s1 : ",s1, "s1의 자료형 : ",type(s1))  #class 'set'
print("l1 : ",l1, "l1의 자료형 : ",type(l1))  #class 'list'
print("t1 : ",t1, "t1의 자료형 : ",type(t1))  #class 'tuple'


# 2. dict (딕셔너리)
#   - 딕셔너리 요소는 key, value 한쌍으로 이루어진 데이타
#  1) dict의 선언
#    변수 이름 = {key : value, key : value, ...}
d1 = { 1: "python", 2: "c", 3: "java"}   # 3개의 데이타
                   # key 는 중복 불가, value 는 중복 가능 (id, pw로 생각하면 됨!)
print(d1)
print(type(d1))   #<class 'dict'>

#  2) Key -> Value
#    변수이름[Key]  -> Key에 해당하는 Value 갑을 가져올 수 있다.
print("Key : 1 , Value : ",d1[1])

#    변수이름[Key] = Value  -> Key에 해당 Value 값을 수정할 수 있다.
d1[1] = "R"
print("Key : 1 , Value : ",d1[1])
#    del 변수이름[Key]   --> 해당 데이터 삭제
del d1[2]
print(d1)

#  3) 딕셔너리 관련 메서드
#    dict.keys()  -> 해당 딕셔너리의 key list 반환
#    dict.values() -> 해당 딕셔너리의 value list 반환
print(d1.keys())
print(d1.values())
#    dict.items()  -> 해당 딕셔너리의 (key,value) list 반환
print(d1.items())

#    dict.get(key)  -> Key에 해당하는 value 값 반환 (dict[key]와 동일)

#[특정 요소의 포함 여부]
#   key in 변수이름
print(1 in d1)





 
