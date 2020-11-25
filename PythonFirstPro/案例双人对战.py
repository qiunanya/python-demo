# 决战紫禁之巅有两个人物，西门吹雪和叶孤城
# 属性：
# name 玩家名字
# blood 玩家血量
#
# 方法：
# tong() 桶对方一刀，对方掉血10滴
# kanren() 砍对方一刀，对方掉血15滴
# chiyao() 吃一颗药，补血10滴
# __str__ 打印玩家状态

# 定义一个类，角色类
# 导入时间的库
import time
class Role:
    def __init__(self, name, blood):
        """
        构造函数初始化
        :param name 角色名
        :param hp 血量
        """
        self.name = name
        self.blood = blood
        pass
    def tong(self, enemy):
        """
        桶一刀
        :param enemy: 敌人
        :return:
        """
        enemy.blood -= 10
        info = "[%s]捅了[%s]一刀" %(self.name, enemy.name)
        print(info)
        pass
    def kanren(self, enemy):
        """
        砍人
        :param enemy: 敌人
        :return:
        """
        enemy.blood -= 15
        info = "[%s]捅了[%s]一刀" % (self.name, enemy.name)
        print(info)
        pass
    def chiyao(self):
        """
        吃药补血
        :param enemy: 敌人
        :return:
        """
        self.blood += 10
        info = "[%s]吃了一颗补血药增加了10滴血" % (self.name)
        print(info)
        pass
    # 设置对象打印格式，类似Java的tostring方法
    def __str__(self):
        return '%s 还剩下 %s 血量'%(self.name, self.blood)


# 创建两个实例化对象,西门吹雪和叶孤城
xmcx = Role('西门吹雪', 100)
ygc = Role('叶孤城', 100)
totalTime = 0.0
while (True):
    start = time.time()
    if xmcx.blood < 0 or ygc.blood < 0:
        break
    if xmcx.blood < 20 or ygc.blood < 20:
        print('%s 快要死了' %(xmcx.name or ygc.name))
    # 西门吹雪捅了叶孤城一刀
    xmcx.tong(ygc)
    # 打印对象状态
    print(ygc)
    print(xmcx)
    print('-------------------------------------')
    # 叶孤城砍了西门吹雪一刀
    ygc.kanren(xmcx)
    # 打印对象状态
    print(xmcx)
    print(ygc)
    # 叶孤城吃药
    ygc.chiyao()
    # 打印对象状态
    print(ygc)
    print(xmcx)
    time.sleep(2)
    end = time.time()
    totalTime = (end - start) + totalTime
    pass
print('游戏结束啦---------')
print('游戏时间为 %f' % round(totalTime, 2), 's')
