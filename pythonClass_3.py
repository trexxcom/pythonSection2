# 클래스 변수, 인스턴스 변수
class Warehouse:
    stockNum = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stockNum += 1

    def __del__(self):
        Warehouse.stockNum -= 1

user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name)
print(user2.name)

print(user1.__dict__)
print(user2.__dict__)

print(Warehouse.__dict__) # 인스턴스 네임스페이스 -> 클래스 네임스페이스, 츨래스 변수(공유)

print(user1.stockNum)
print(user2.stockNum)
