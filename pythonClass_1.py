class UserInfo:
    def setInfo(self, name, phone):
        self.name = name
        self.phone = phone

    def printInfo(self):
        print('--------------')
        print('Name: ' + self.name)
        print('Phone: ' + self.phone)
        print('--------------')

user1 = UserInfo()
user2 = UserInfo()

print(id(user1))
print(id(user2))

user1.setInfo("kim","010-3433-7777")
user2.setInfo("park","010-7777-7777")

user1.printInfo()
user2.printInfo()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)
print(user2.phone, user2.name
