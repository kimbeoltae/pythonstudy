#list [] 순서를 따지는 객체의 집합

subway = [10, 20, 30]
print(subway)

subway = ['유재석', '박명수', '정준하']
print(subway)

#명수옹 몇번째칸?
print(subway.index('박명수'))

#하하가 다음 정류장에서 다음 칸에 탐
subway.append('하하')
print(subway)

#형돈이 유/박 사이에 탐
subway.insert(1, '정형돈')
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

#같은 이름 사람이 몇 명 있는지
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)

#딕셔너리
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet[5])
print('hi') # 위 라인에서 오류가 떠서 출력이 안 되지만

print(cabinet.get(5))
print('hi') # 여긴 위 라인에 none이라 뜨고 hi 출력이 됨

print(cabinet.get(5, "사용 가능")) #5 없으니 사용 가능을 출력

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())
#value들만 출력
print(cabinet.values())
#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)

#튜플 -> 내용 변경, 추가 불가 / 리스트보다 빠름
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") < error

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#세트(집합) 중복x 순서x
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "조세호"}
python = set(["유재석", "박명수"])

#교집합(java, python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 java할 수 있거나 python 할 수 있는 개발자
print(java | python)
print(java.union(python))

#차집합 java 할 수 있지만 python은 할 줄 모르는 개발자
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java 까먹었어요
java.remove("김태호")
print(java)

#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#Quiz
from random import *
users = range(1,21) #1~20
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명 중 1명 치킨, 3명 커피
print('-- 당첨자 발표 --')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print('-- 축하합니다 --')

