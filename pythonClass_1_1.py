class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def printInfo(self):
        print('--------------')
        print('Name: ' + self.name)
        print('Phone: ' + self.phone)
        print('--------------')

    def __del__(self):
        print("delete!")

user1 = UserInfo("kim","010-3433-7777")
user2 = UserInfo("park","010-7777-7777")

print(id(user1))
print(id(user2))

# user1.setInfo("kim","010-3433-7777")
# user2.setInfo("park","010-7777-7777")

user1.printInfo()
user2.printInfo()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)
