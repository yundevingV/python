#오늘의 속담

import random

quotes = ["꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다",
          "사람은 사랑할 때 누구나 시인이 된다",
          "고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다",
          "시작이 반이다"]

dailyquotes = random.choice(quotes)

print("######################")
print("# 오늘의 속담 #")
print("######################")
print(dailyquotes)
>>>
######################
# 오늘의 속담 #
######################
꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다

#딕서녀리
딕셔너리는 value와 관련된 key가 있다.

phonebook = {}

phonebook["홍길동"] = "010-1234-5678"

print(phonebook)
>>>
{'홍길동': '010-1234-5678'}

이렇게 딕셔너리를 추가 할 수 있다.

phonebook = {"홍길동" : "010-1234-5678" , "이순신" : "010-123-567"}

print(phonebook)
이런식으로도 추가할 수 있다.

#딕셔너리 연산

phonebook = {"홍길동" : "010-1234-5678" , "이순신" : "010-123-567"}

print(phonebook["홍길동"])
>>>
010-1234-5678

키(key)값을 가지고 value값을 찾을 수 있다.

phonebook = {"홍길동" : "010-1234-5678" , "이순신" : "010-123-567"}

print(phonebook.keys())
print(phonebook.values())
>>>
dict_keys(['홍길동', '이순신'])
dict_values(['010-1234-5678', '010-123-567'])

phonebook 딕셔너리에 저장된 모든 키값과 밸류값을 출력할 수 있다.

dict = {'name' : '홍길동' , 'age' : '20' , 'major' : 'csie'}

print(dict['name'])
>>>
홍길동

#딕셔너리 연산2

phonebook = {"이순신" : "010-123-567" , "홍길동" : "010-1234-5678"}

for key in sorted(phonebook.keys()):
    print(key, phonebook[key])
>>>
이순신 010-123-567
홍길동 010-1234-5678

딕셔너리의 모든 항목을 방문하면서 출력하기.

phonebook = {"이순신" : "010-123-567" , "홍길동" : "010-1234-5678"}

del phonebook["이순신"]
print(phonebook)
>>>
{'홍길동': '010-1234-5678'}

딕서녀리의 항목 삭제하기.

phonebook = {"이순신" : "010-123-567" , "홍길동" : "010-1234-5678"}

phonebook.clear()
print(phonebook)
>>>
{}

딕셔너리의 항목 비우기.
