#편의점 재고관리

items = {"커피음료" : 7, "펜" : 3, "종이컵" : 2, 
         "우유" : 1, "콜라" : 4, "책" : 5}

a = input("물건의 이름을 입력하시오 : ")

print(items[a])
>>>
물건의 이름을 입력하시오 : 콜라
4

#영한사전

english_dict = {}

english_dict["one"] = '하나'
english_dict["two"] = '둘'
english_dict["three"] = '셋'

a = input("단어를 입력하시오 : ")

print(english_dict[a])

//문제에서 공백 딕셔너리로 만들라해서..

#연습문제 p276~
1.
numbers = [] 
count = 0

while count < 5 :
    number = int(input("정수를 입력하시오 : "))
    numbers.append(number)
    count = count +1

avg = sum(numbers) / len(numbers)
print("평균 :" , avg)
>>>
정수를 입력하시오 : 10
정수를 입력하시오 : 20
정수를 입력하시오 : 30
정수를 입력하시오 : 40
정수를 입력하시오 : 50
평균 : 30.0
         
2.
import random

count = 0
n = [0, 0, 0, 0, 0, 0]

while count < 1000:
    a = random.randint(0,5)
    n[a] = n[a] +1
    count = count + 1 
     
print("주사위 1인 경우는 : ", n[0])
print("주사위 2인 경우는 : ", n[1])
print("주사위 3인 경우는 : ", n[2])
print("주사위 4인 경우는 : ", n[3])
print("주사위 5인 경우는 : ", n[4])
print("주사위 6인 경우는 : ", n[5])
>>>
주사위 1인 경우는 :  189
주사위 2인 경우는 :  178
주사위 3인 경우는 :  146
주사위 4인 경우는 :  175
주사위 5인 경우는 :  152
주사위 6인 경우는 :  160
