# 1) 사람 클래스
class Person:
    # 이름, 나이, 성별
    # name, age, gender
    # 1-1) 새로 만들 때 입력
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
# 2) 직장 동료 클래스
# 상속
class Colleague(Person):
    # 2-1) 기본 직급 대리
    # position = "대리"
    # 2-2) 새로 만들 때 입력
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position

colleague = Colleague("sunyoung", 28, "female", "대리")
# print(colleague.name)
print(colleague.__dict__)
