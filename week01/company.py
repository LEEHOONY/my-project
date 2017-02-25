# 회사 조직도 만들기
# 사람 클래스를 만든다(사람의 기본요소는 이름, 나이, 성별로 한다)
# 직장 동료 클래스를 사람 클래스를 이용하여 만든다.(사람 기본 요소 외 직급을 추가한다.)

## Human class
class Human:
    company = "Python"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

human1 = Human("홍길동", "23", "M")
human2 = Human("장희빈", "21", "F")
human3 = Human("임꺽정", "32", "M")

print(human2.name)
print(human3.sex)

## Colleague class
class Colleague(Human):
    designation = "부장"

colleague = Colleague("이순신", "40", "M")
print(colleague.name)
print(colleague.designation)
