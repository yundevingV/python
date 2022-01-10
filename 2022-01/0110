#난수 생성

import random

print("동전 던지기 게임을 시작합니다")

coin = random.randrange(2)

if coin == 0 :
    print("앞면입니다")
else :
    print("뒷면입니다")
    
 #import random을 한후 random.randrange(x)를 변수에 저장해주면 0에서 x만큼의 숫자가 랜덤으로 나오게 된다.
 
 #elif
 
num = int(input("숫자를 입력하시오."))

if num > 0 :
    print("양수입니다")
elif num ==0 :
    print("0입니다")
else :
    print("음수입니다")
>>>
숫자를 입력하시오.0
0입니다

if문에서 다른 조건을 검사 할 수 있다.

#로그인 프로그램

id = "ys0222"
passward ="1234"

a = input("아이디를 입력하시오.")
b = input("패스워드를 입력하시오.")

if ((a == id) and (passward == b)) :
    print("로그인 되셨습니다.")
elif a != id  :
    print("아이디를 확인해주세요.")
elif b != passward :
    print("패스워드 확인해주세요.")
else :
    print("아이디와 패스워드를 확인해주세요.")
    
    id = "ys0222"
passward ="1234"

a = input("아이디를 입력하시오.")
b = input("패스워드를 입력하시오.")

if ((a == id) and (passward == b)) :
    print("로그인 되셨습니다.")
elif a != id  :
    print("아이디를 확인해주세요.")
elif b != passward :
    print("패스워드 확인해주세요.")
else :
    print("아이디와 패스워드를 확인해주세요.")

#page 153

1.
age = 20
if age < 20:
  print('20살 미만')
else :
  print('20살 이상')
>>>
20살이상

2.
age = 20

if (age >= 30 and age <= 50) :
  print('30살 이상 50살 이하')
  
else :
  print('30살과 50살 사이가 아님')
>>>
30살과 50살 사이가 아님

3.
temp =  int(input("현재 온도를 입력하시오"))

if temp >= 25 :
    print("반바지를 입으세요")
else :
    print("긴바지를 입으세요")
>>>
현재 온도를 입력하시오30
반바지를 입으세요

4.
score =  int(input("성적을 입력하시오."))

if (score >=90 and score <=100) :
    print("A학점입니다.")
elif (score >=80 and score <90) :
    print("B학점입니다.")
elif (score >=70 and score <80) :
    print("C학점입니다.")
elif (score >=60 and score <70) :
    print("D학점입니다.")
else :
    print("F학점입니다.")
>>>
성적을 입력하시오.80
B학점입니다.

5.
import random

x =random.randint(1,100)
y =random.randint(1,100)

print(x,"-",y,"=")
a=int(input())
if x-y == a :
    print("맞았습니다")
else :
    print("틀렸습니다")
>>>
67 - 60 =
7
맞았습니다

6.
a= int(input("정수를 입력하시오:"))

if (a % 2 ==0 ) and (a % 3 ==0) :
    print("2와 3으로 나누어 떨어집니다")
else :
    print("틀렷습니다")
>>>
정수를 입력하시오:30
2와 3으로 나누어 떨어집니다

7.
import random
x = random.randint(1,100)

lotto = int(input("복권번호를 입력하시오 (0에서 99사이)"))
print("당첨번호는", x , "입니다")
if lotto == x :
    print("상금은 100만원 입니다")
elif (x % 10 == lotto // 10) or (x %10 == lotto %10) :
    print("상금은 50만원 입니다")
elif (x // 10 == lotto // 10) or (x //10 == lotto %10) :
    print("상금은 50만원 입니다")
else :
    print("꽝")
>>>
복권번호를 입력하시오 (0에서 99사이)85
당첨번호는 3 입니다
꽝
복권번호를 입력하시오 (0에서 99사이)85
당첨번호는 75 입니다
상금은 50만원 입니다
