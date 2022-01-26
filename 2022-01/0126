#함수 안에서 전역변수 사용하기

def calculate_area (radius):
    global area
    area = 3.14 * radius **2
    return

area  = 0
r = float(input("원의 반지름"))
calculate_area(r)
print(area)
>>>
원의 반지름3
28.26

함수 안에서 변수앞에 'global'이라고 적어주면된다.

#디폴트 인수

def greet(name,msg):
    print("안녕", name + ',' + msg)

greet("철수","안녕")
>>>
안녕 철수,안녕

인수를 전달받아서 함수를 실행시킨다.

#page226

5.
def happyBirthday(name):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear" , name)
    print("Happy Birthday to you!")

happyBirthday("홍길동")
>>>
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear 홍길동
Happy Birthday to you!

6.
def plus(a,b):
    print("정수",a,"+",b,"의 합은?")
    return

a = int(input("첫번째정수"))    
b = int(input("두번째정수"))
    
plus(a,b)
>>>
첫번째정수10
두번째정수20
정수 10 + 20 의 합은?

7.
pi = 3.14

def circleArea(r):
    global area
    area = pi * r**2
    return

def circleCircumference(radius):
    global circle
    circle = r * 2
    return

r = float(input(""))
circleArea(r)
print("반지름이",r,"인 원의 면적",area)

radius = float(input(""))
circleCircumference(radius)
print("반지름이",r,"인 원의 둘레",circle)
>>>
10
반지름이 10.0 인 원의 면적 314.0
10
반지름이 10.0 인 원의 둘레 20.0
