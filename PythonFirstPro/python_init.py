class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        pass

    def eat(self):
        print(self.name + '喜欢吃榴莲')
    pass


# qiu = Person()
# qiu.name = '邱南亚'
# qiu.sex = '男'
# qiu.age = 20
# qiu.eat()
#
# mei = Person()
# mei.name = '小美'
# mei.age = 21

# print(qiu, qiu.age, qiu.sex, qiu.name)

# 初始化赋值
bai = Person('东方不败', 22, '男')
print('init 初始赋值，类似java ', bai.name, bai.age, bai.sex)
bai.eat()


