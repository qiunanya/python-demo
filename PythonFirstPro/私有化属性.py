# 私有化属性，两个下划线开头 __age:20 不能在外部直接访问，在类的内部是可以访问的
class Person:
    def __init__(self):
        self.__name = '李四' # 加两个下划线，将此属性私有化，不能在外部直接访问，在类的内部是可以访问的
        self.age = 24
    pass

    def __str__(self):
        return '{} 的年龄是 {}'.format(self.__name, self.age)
    pass

xl = Person()
# print(xl.__name)
print(xl)