try:
    f=open('none', 'r')         #파일 open 시도
except FileNotFoundError as e:  #파일을 못 찾으면 FileNotFoundError 출력
    print(str(e))
else:                           #open 성공하면 실행
    data = f.read()
    print(data)
    f.close

