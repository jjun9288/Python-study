#반복되는 변수 & 메서드(함수)를 하나의 설계도로 미리 정해놓는 틀

#ex) 계산기
class Calculator:       #틀
    def __init__(self,first,second):    #생성자 (제일 처음 실행 됨)
        self.first = first
        self.second = second

    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

cal1 = Calculator()     #틀에서 찍어내는 과자

cal1.setdata(3,4)      #self 에 cal1, first에 3, second에 4가 들어가는 것
print(cal1.add())

#상속
class Fourcal(Calculator):      #자식같은 개념. 부모를 이용하여 다른 틀을 만들 수 있음
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
    
    def power(self):
        result = self.first ** self.second
        return result

#메서도 오버라이딩 - 자식이 부모를 덮어 씀
a = Fourcal(4,0)
print(a.div())



