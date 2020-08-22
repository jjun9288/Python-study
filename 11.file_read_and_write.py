#Writing mode
f = open("새파일.txt", 'w') 
for i in range(1,11):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)
f.close()

#Reading mode
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

 #Add mode  (close할 필요 없음)
 with open("foo.txt", "w") as f:
    f.write("Jun Young Yoon")

