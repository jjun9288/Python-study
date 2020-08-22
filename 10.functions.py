def sum(a,b):
    result = a+b
    return result
print(sum(1,2))

#입력값이 없는 함수
def say():
    return 'Hi'

print(say())

#결과값이 없는 함수
def sum(a,b):
    print("%d, %d의 합은 %d 입니다." % (a,b,a+b))
    
sum(1,2)
    #return 값은 없으므로 print를 찍어보면 none 이 나온다.

#입력값도 결과값도 없는 함수
def say():
    print('Hi')
    #none

#여러 개의 입력값 (args)
def sums(*args): #->몇 개가 들어가든 상관없다
    sum = 0
    for i in args:
        sum += i
    return (sum)
print(sums(1,3,5))

#함수 골라서 사용하기
def sum_and_mul(a,b):
    return a+b, a*b, a/b
print(sum_and_mul(1,2)[0])

#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다" %name)
    print("나이는 %d 입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("윤준영",26)    #return 값은 없으므로
                #-> 인자에 3개를 안 넣었는데 실행되는 이유는 기본 값으로 True를 
                #   해두었기 때문이다.

#lambda

add = lambda a,b: a+b
print(add(1,2))     #-> def add(a,b):
                    #       return a+b 와 같다고 보면 된다