#사용자가 입력하는 숫자의 합 계산하기

answer  = 'yes'
sum =0
num=0

while(answer == 'yes'):
    num = int(input("숫자를 입력하시오"))
    answer = input("계속?(yes or no)")
    sum += num

print(sum)
>>>
숫자를 입력하시오3
계속?(yes or no)yes
숫자를 입력하시오5
계속?(yes or no)yes
숫자를 입력하시오7
계속?(yes or no)no
15

#숫자맞추기 게임

import random

print("1부터 100사이의 숫자를 맞추시오.")

count = 0
rn = random.randint(1,101)
answer=0
while (answer != rn):
    answer =int( input("숫자를 입력하시오"))
    count = count +1
    if (rn < answer):
        print("낮음!")
    else :
        print("높음!")

print("축하합니다. 시도횟수 =",count)
>>>
1부터 100사이의 숫자를 맞추시오.
숫자를 입력하시오52
낮음!
숫자를 입력하시오1
높음!
숫자를 입력하시오2
높음!
숫자를 입력하시오30
높음!
축하합니다. 시도횟수 = 5
