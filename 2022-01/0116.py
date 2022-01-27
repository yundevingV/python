#while 반복문

 while 조건:
    반복 문장
이런식으로 구성되어있다.

#로그인 프로그램

password = "";
while password != "ys":
    password = input("암호를 입력하시오")
print("로그인 성공")
>>>
암호를 입력하시오123
암호를 입력하시오ys
로그인 성공
 
#1부터 10까지 합구하기

count = 1
sum = 0

while count <=10:
    sum = sum +count
    count = count +1
print(sum)
>>>
55

#구구단출력
num = int(input("원하는 단은:"))

count = 1
while count < 10:
    print(num,"*",count,"=",num*count)
    count = count +1
>>>
원하는 단은:1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
