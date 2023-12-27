jumin = "990229-1234567"
print("성별 식별번호 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("주민번호 뒷자리 : " + jumin[7:])
print("주민번호 뒷자리(뒤에서부터) : " + jumin[-7:])

fruit = "apple"
print(fruit[:5])

python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[1:3].islower())
print(python.replace("Python", "Java"))
