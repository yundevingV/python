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

3.
dict = {}

while True:
    name = input("(입력모드) 이름을 입력하시오 : ")
    if not name :
        break;
    tel = input("전화번호를 입력하시오")
    dict[name] = tel
    

searching = input("(검색모드) 이름을 입력하시오")

print(searching ,"의 전화번호는", dict[searching], "입니다")
>>>
(입력모드) 이름을 입력하시오 : 홍길동
전화번호를 입력하시오111-2222
(입력모드) 이름을 입력하시오 : 김철수
전화번호를 입력하시오222-3333
(입력모드) 이름을 입력하시오 : 
(검색모드) 이름을 입력하시오홍길동
홍길동 의 전화번호는 111-2222 입니다

7.
dict = {"kr" : "대한민국", "sk" : "슬로바키아", "no" : "노르웨이",
        "jp" : "일본", "hu" : "헝가리", "de" : "독일",}

for key, value in dict.items():
    print(key, ":", value)
>>>
kr : 대한민국
sk : 슬로바키아
no : 노르웨이
jp : 일본
hu : 헝가리
de : 독일
         
###딕셔너리 뒤집기

dict = {"kr" : "대한민국", "sk" : "슬로바키아", "no" : "노르웨이",
        "jp" : "일본", "hu" : "헝가리", "de" : "독일",}
new_dict = {}
for i, j in dict.items():
    new_dict[j] = i
    
print(new_dict["일본"])
>>>
jp
원하는 키값을 출력하고 싶을때 사용하면 유용할듯 !

8.
import random

problems = {'파이썬' : '최근에 가장 떠오르는 프로그래밍 언어',
            '변수' : '데이터를 저장하는 메모리 공간',
            '함수' : '작업을 수행하는 문장들의 집합에 이름을 붙인것',
            '리스트' : '서로 관련이 없는 항목들의 모임'}

new_problems = {}
for i, j in problems.items():
    new_problems[j] = i
r = ['파이썬', '변수', '함수', '리스트']    


while True:
    choicelist = random.choice(r)
    print("다음은 어떤 단어에 대한 설명일까요?")
    print(problems[choicelist])
    print("(1) 파이썬 (2) 함수 (3) 리스트 (4) 변수")
    b = input("")
    if b == choicelist :
        print("맞았습니다")
    else :
        print("틀렸습니다")
>>>
다음은 어떤 단어에 대한 설명일까요?
최근에 가장 떠오르는 프로그래밍 언어   
(1) 파이썬 (2) 함수 (3) 리스트 (4) 변수
파이썬
맞았습니다
다음은 어떤 단어에 대한 설명일까요? 
최근에 가장 떠오르는 프로그래밍 언어
(1) 파이썬 (2) 함수 (3) 리스트 (4) 변수
파이썬
맞았습니다
다음은 어떤 단어에 대한 설명일까요?
서로 관련이 없는 항목들의 모임
(1) 파이썬 (2) 함수 (3) 리스트 (4) 변수
리스트
맞았습니다

//turtle, tkinter 제외한 파이썬 컨텐츠는 완료!
