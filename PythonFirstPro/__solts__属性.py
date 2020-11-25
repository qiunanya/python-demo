# __slots__ 动态添加对象属性, 可以限制属性添加属性规则，没有的无法添加
class Student(object):
    __slots__ = ('name', 'age', 'height')

    def __str__(self):
        return '{} 年龄{} 身高{}'.format(self.name, self.age, self.height)
    pass

xm = Student()
xm.name = '小明'
xm.age = 21
xm.height =1.65
# print(xm.__dict__) # 所有可用属性都在这里存储，占用空间大，有了__slots__，就不需要__dict__ 二者会冲突
print(xm)

class Sub(Student):
    # __slots__ = () # 子类没有开启__slots__时可以自定义属性，开启__slots__后无法自定义，因为继承了父类
    pass
s = Sub()
s.gender = '男'
s.pro = '大数据'
print(s.gender,s.pro)