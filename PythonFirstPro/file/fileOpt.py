# 文件的操作, 打开，读写，关闭
# 'r' 'r+' 读取（默认）,只读，适用普通场景
# 'w' 'wb+' 'w+' 写入，每次会覆盖原有内容，没有则创建文件
# 'x'排它性创建，如果文件已存在则失败
# 'a' 'ab' 'a+' 追加，不会覆盖原有内容，如果文件存在则在末尾追加
# 'b'二进制模式
# 't'文本模式（默认）
# '+'打开用于更新（读取与写入）
# 'rb' 'rb+' 使用于文件 图片 视频 音频 这样的文件读取

# 打开文件
# fobj = open('./test.txt', 'w', newline='', encoding='utf-8')
# # 开始读/写操作
# fobj.write('非宁静无以致远，非淡泊无以明志')
# fobj.write('狂风卷积着乌云 \n')
# # 关闭文件
# fobj.close()

# 以二进制形式区写数据
# fobj = open('test.txt', 'wb')
# fobj.write('以二进制形式区写数据'.encode('utf-8'))
# fobj.close()

# a 追加文本内容到尾部
fobj = open('test.txt', 'a', encoding='utf-8')
fobj.write('a 追加文本内容到尾部\n')
fobj.write('a 送的话费送货奋斗和\r')
fobj.close()

# 'r' 读取文件内容操作
fobj = open('test.txt', 'r', encoding='utf-8')
# red = fobj.read() #不传参数默认读取全部数据
red = fobj.read(20) # 读取20个字符，从头开始读取
print(red)
print(fobj.readline()) #读一行
fobj.close()

# with 上下文管理对象, 自动释放管理对象
with open('test.txt', 'a', encoding='utf-8') as ff:
    # print(ff.read())
    # print(ff.readline())
    ff.write('with 写入内容')
    pass



