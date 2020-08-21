# 2. Tuple
#   -> list 와 거의 동일함 
#   list vs tuple
#   -list는 값을 변경할 수 있고, tuple은 값을 변경할 수 없다.
#   - 실행 속도 : tuple > list
#     -> 프로그램이 실행되는 동안 그 값을 유지해야 할 땐 tuple로 저장
#                                그 값이 변경될 수 있는 데이타는 list로 저장

#  1) 튜플의 선언
t1 = (1,2,"three",4,5)  # tuple은 소괄호, list는 대괄호
print(type(t1))   # <class 'tuple'>

#  2) 튜플의 인덱싱
#    변수 이름 [index]
print("0번째 데이타 : ",t1[0])

#  3) 튜플의 슬라이싱
#    변수이름[시작위치:끝위치]
print(t1[:3])
    
# [튜플의 복사]
#t2 = t1
t2 = t1[:]
print(t1, t2)
print(id(t1), id(t2))   # 같은 주소값 나옴

# 값을 변경 할 수 없다.
# t1[0] = 100 or "hello" -> ERROR

# 자료형
#   - 숫자 자료형 : int, float
#   - 시퀀스 자료형
#       - 가변 시퀀스 : list
#       - 불변 시퀀스 : str, tuple, range
#   - 집합 자료형 : set
#   - 매핑 자료형 : dict


# 시퀀스 자료형
#   인덱싱이 가능하다 : 변수이름[index]
#   슬라이싱이 가능하다 : 변수이름[index:index]
#   요소 in 변수이름 ?
#   요소 not in 변수이름 ?
#   + : 연결하기
#   * : 반복하기
#   변수이름.index(요소) -> 요소의 위치
#   변수이름.count(요소) -> 요소의 갯수
#   함수 len(시퀀스 자료형) -> 길이
#                               -> 문자열이면 문자열 길이,
#                                    tuple, list 이면 칸의 갯수
print(len(t1))

#[패킹과 언패킹] 파이썬만의 독특한 문법
# 1) 패킹
#   변수 이름 = data, data, data
arr1 = 20,"hello",100,300  #소괄호, 대괄호가 없으면 튜플로 인식함!<class 'tuple'>
print(type(arr1))

arr1 =  20,"hello",100,300  #tuple
arr1 = (20,"hello",100,300) #tuple
arr1 = [20,"hello",100,300] #list

# 2) 언패킹
a,b,c,d = arr1
print("a:",a, "b:",b, "c:",c, "d:",d)  #a: 20 b: hello c: 100 d: 300

#a,b,c = arr1  or a,b,c,d,e,f = arr1-> ERROR, 갯수를 맞춰야 함!


#estrellita12@naver.com


