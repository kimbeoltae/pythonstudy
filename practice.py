#자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print(5 > 10)
print(5 < 10)
print(not True)
print(not (5 > 10))
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3
print('우리집' + animal + '의 이름은 ' + name +'예요.')
print(name + '는' + str(age) + '살이며,' + hobby + '를 아주 좋아해요.')
print(name + '는 어른일까요?' + str(is_adult))

station = '사당'
print(station + '행 열차가 들어오고 있습니다.')

print(1+1)
print(5%3)
print(5//3)
print(3 == 3)
print(1 != 3)
print(not 1 != 3)

print(abs(-5)) #절댓값
print(pow(4,2)) #4^2
print(max(5,12))
print(min(5,12))
print(round(3.14)) #반올림
print(round(4.99))

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

from random import *
print(random()) #0.0~1.0 임의의 값 생성
print(random())
print(random() * 10)
print(int(random()*10))

print(int(random() * 45 ) + 1) #1~45이하 임의의 값 생성
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)

print(randrange(1,46)) #1~45이하 임의의 값 생성

print(randint(1,45)) #45포함!

print('오프라인 스터디 모임 날짜는' + str(randint(4,28)) + '일로 선정되었습니다.')

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """나는 소년이고,파이썬은 쉬워요"""
print(sentence3)

jumin = "990120-1234567"
print('성별 : ' + jumin[7])
print('연 : ' + jumin[0:2])
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])
print('생년월일 : ' + jumin[0:6])
print('생년월일 : ' + jumin[:6])

print('뒤 7자리 :' + jumin[7:14])
print('뒤 7자리 :' + jumin[7:])
print('뒤 7자리 (뒤에서부터) :' + jumin[-7:])

#문자열 처리 함수
python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'C'))
index = python.index('n')
print(index)
index = python.index('n', index + 1)
print(index)
print(python.find('C')) #값 없으면 -1 반환
# print(python.index('C')) #값 없으면 error
print(python.count('n'))

#문자열 포맷
print('a' + 'b')
print('a', 'b')
#way1
print('나는 %d살 입니다.' %20) #d 정수
print('나는 %s을 좋아해요.' %'파이썬') #s 문자열
print('Apple은 %c로 시작해요.' %"A") #c 캐릭터 한 글자만

print('나는 %s색과 %s색을 좋아해요.' % ('파란','빨간'))
#way2
print('나는 {}살 입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란','빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란','빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란','빨간'))

#way3
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color='빨간'))

#way4 (v3.6 이상)
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')

#탈출문자
print('백문이 불여일견\n백견이 불여일타')
#\n 줄바꿈

#저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
#\" \' : 문장 내에서 따옴표

#\\ : 문장 내에서 \
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b : 백스페이스(한 글자 삭제)
print("Redd\bApple")

#\t : 탭
print("Red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# r1) http:// 부분은 제외 -> naver.com
# r2) 처음 만나는 점(.) 이후 부분은 제외 -> naver
# r3) 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e' 개수 + '!'로 구성
#              nav                 5         1                  !
# 생성된 비밀번호 : nav51!

# url = "http://naver.com"
# url = "http://daum.net"
url = "http://google.com"
my_str = url.replace("http://", "") #r1
print(my_str)
my_str = my_str[:my_str.index(".")] #r2
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

