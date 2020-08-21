#While문
#ex) 1,2,3,4,5,...,100까지 출력하세요.

i=1
while i<=100:
    print(i)
    i=i+1


i=1
while i<=9:
    print("2 x %d = %d"%(i,2*i))
    i += 1


#ex) while 문을 이용해서 1부터 100까지의 합을 출력하세요

sum=0
i=1
while i<=1000:
    sum=sum+i
    i+=1
print("sum = ",sum)

#ex) 5개의 성적을 입력받고, 성적의 총합을 출력하세요.

sum=0
i=1
while i<=5:
    g=int(input(str(i)+"번째 성적 : "))  #int(input(i,"번째성적:")) ->ERROR
    sum += g
    i += 1
print("총합 : ",sum)


#무한루프 (끝나지 않는 반복문 ( 조건식이 영원히 참인 반복문))

while True :
    수행할 문장
    반복문을 끝낼 조건식 -> break




