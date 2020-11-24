# 类属性和类方法
class People:
    country = 'china'
    # @classmethod 类方法申明
    @classmethod
    def get_contry(cls):
        return cls.country # 访问类方法
        pass
    @classmethod
    def change_contry(cls, name):
        cls.country = name # 修改类属性的值
        pass
    # @staticmethod 静态方法，充分利用对象资源
    @staticmethod
    def get_Data(obj):
        return People.country + obj
        pass
    pass

# 类调用类方法
print(People.get_contry(), People.change_contry('邱南亚'), People.get_Data('静态方法调用'))
# 实例对象调用类方法
p = People()
print(p.get_contry())

# 返回当前系统时间
import time
class currentTime:
    def __init__(self, hour, min, second):
        self.hour = hour
        self.min = min
        self.second = second
        pass

    # 独立静态方法，无参
    @staticmethod
    def showTime():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pass
    pass

    # 独立静态方法，有参
    @staticmethod
    def add(x, y):
        return x+y
        pass


print(currentTime.showTime(), currentTime.add(1, 87))

