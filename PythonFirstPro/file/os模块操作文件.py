# 文件操作模块
import os
import shutil
# 获取项目路径
# os.path.realpath(_file_)——返回真实路径
# os.path.split()——返回路径的目录和文件名
# os.getcwd()——得到当前工作的目录
print(os.path.realpath(__file__))
print(os.path.split(os.path.realpath(__file__)))
print(os.getcwd())

# 路径拼接
print(os.path.join(os.getcwd(), 'qiu'))

# # 重命名
# os.rename('test_重命名.txt', 'test.txt')

# 删除
# os.remove('D:\python-demo\PythonFirstPro\fileqiuqiu')

# 创建文件夹 mkdir只能创建一级目录
# os.mkdir(os.getcwd()+'/qiu')

# makedirs 可以创建多级文件
# os.makedirs('d:/python测试文件夹/spring/dubbole')

# 只能删除空目录
# os.rmdir('d:/python测试文件夹')

# 如果需要删除非空目录，需要引入shutil模块, 多级删除
# shutil.rmtree('d:/python测试文件夹')

# 获取python中的目录列表
# listrs = os.listdir('d:/')
# for i in listrs:
#     print(i, len(i))
#     pass

# 现代版目录获取scan
# with os.scandir("d:/demo") as enlist:
#     for entry in enlist:
#         print(entry.name, len(entry.name))
#         pass
#     pass

# 判断是文件还是文件夹
basePath = 'd:/demo'
print(os.listdir(basePath))
for file in os.listdir(basePath):
    if os.path.isfile(os.path.join(basePath, file)):
        print('文件：{}'.format(file))
    if os.path.isdir(os.path.join(basePath, file)):
        print('文件夹：{}'.format(file))
    pass