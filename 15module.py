# math
# import math
# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
# print(math.floor(14.844))#내림처리
# print(math.ceil(14.144)) #올림처리
import datetime
# from
from math import sin, cos, floor, ceil
# print(sin(1))
# print(cos(1))
# print(tan(1))
# print(floor(14.844))#내림처리
# print(ceil(14.144)) #올림처리

# from alias
import math as m
# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
# print(math.floor(14.844))#내림처리
# print(math.ceil(14.144)) #올림처리

# random
import random
import math

# print(random.random())
# print(int(random.random()*10))
# print( math.ceil(random.random()*10))
# print( random.randrange(5)) # 0~4까지 난수
# print( random.randrange(11,22)) # 11~21까지 난수

# li = [10, 20, 30, 40, 50]
# print(random.choice(li)) # 임의의 요소 1개만 선택
#
# random.shuffle(li) # 저장된 요소의 위치를 섞는다.
# print(li)
# print(random.sample(li,k=3))

#sys
# import sys
# print(sys.argv) #실행되는 파일의 경로위치
# print(sys.getwindowsversion()) #버전정보
# print(sys.copyright)
# print(sys.version)
#
# sys.exit(-1) # 현재 구문 강제종료

#os
import os
# print(os.name)
# print(os.getcwd())
# print(os.listdir())
# os.mkdir("test")
# os.rmdir("test")
# if not os.path.exists("test") :
#     os.mkdir("test")
# else:
#     with open("test/abc.txt",'w') as file:
#         file.write("Hello World")
#
# os.rename("test/abc.txt","test/hong.txt")

# os.remove("test/hong.txt") #파일삭제
# os.system("dir")
# os.system("notepad")
# os.system("code .")
# os.system("echo 'test'>haha.txt")

#DateTime
import DateTime
# now = datetime.datetime.now()
# print(now)
#
# one_day_later = now + datetime.timedelta(days=1)
# print(one_day_later)
#
# one_day_week_later = now + datetime.timedelta(weeks=1)
# print(one_day_week_later)
#
# etc_later = now + datetime.timedelta(days=1,weeks=1,hours=1,minutes=1,seconds=1)
# print(etc_later)
#
# two_year_later = now.replace(year=(now.year+2))
# print(two_year_later)

#time
# import time
# nowtime = time.time()
# print(nowtime)
# five_second_later = nowtime+5
#
# while True:
#     print(".", end="")
#     time.sleep(1)
#     if time.time() >= five_second_later :
#         break
# print("종료")

#urllib

from urllib import request

target = request.urlopen("http://google.com")
output = target.read()
print(output)