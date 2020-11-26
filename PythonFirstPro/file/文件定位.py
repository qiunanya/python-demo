# 文件定位
# tell() 返回指针当前所在的位置
# truncate() 截取原文件大小
# seek() 文件定位，文件中光标位置
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read(5))
    print(f.tell())
    pass

print('---------------truncate 截取文件内容-------------------')
fobj = open('test.txt', 'r', encoding='utf-8')
print(fobj.read())
fobj.close()
print('截取内容如下---------------------')
fob = open('test.txt', 'r+', encoding='utf-8')
fob.truncate(15) # 保留前15个字符
print(fob.read())
fob.close()

print('-----------------seek()光标定位文件内容位置---------------------------')
with open('test.txt', 'r', encoding='utf-8') as fobA:
    content = fobA.read(4)
    print(content)
    # 想当于光标又设置到了0的位置
    fobA.seek(0, 1)
    print(fobA.read(3))
    pass
