#반복문

for i in [1, 2, 3, 4, 5] :
    print("hello")
>>>
hello
hello
hello
hello
hello

for i in [1, 2, 3, 4, 5] :
    print("i=",i)
>>>
i= 1
i= 2
i= 3
i= 4
i= 5

#리스트에 숫자들을 저장하고 꺼내 반복하는 방식.

for i in range(5):
    print("방문을 환영합니다")
>>>
방문을 환영합니다
방문을 환영합니다
방문을 환영합니다

#range()함수를 이용해 반복문을 사용할 수 있다.

range(start,stop,step)
start에서 시작해서 stop-1 까지 step 간격으로 정수들이 생성된다.

for i in range(1,6,1):
    print(i)
>>>
1
2
3
4
5

#팩토리얼
a = int(input("정수를 입력하시오."))

b= 1

for i in range(1, a+1,1):
    b = b * i
  
print(a, "!은", b, "이다")
>>>
정수를 입력하시오.10
10 !은 3628800 이다
    
    
