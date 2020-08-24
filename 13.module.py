#모듈 ? 미리 만들어놓은 .py 파일

import mod1
print(mod1.add(2,3))

#mod1에 많은 함수가 있다면 특정 함수만 가져올 수 있다.

from mod1 import add
print(add(2,3))

#원하는 파일이 하위 폴더 안에 있을 경우

import sys
sys.path.append("C:\\python\subfolder")
import mod1

