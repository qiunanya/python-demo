# 小文件自动备份
def copyfile():
    # 接收用户输入的用户名
    old_file = input('请输入文件名....')
    file_list = old_file.split('.')
    print(file_list)
    # 构造新的文件名.加上备份的后缀
    new_file = file_list[0]+'_备份.'+file_list[1]
    # 打开需要备份的文件
    old_f = open(old_file, 'r', encoding='utf-8')
    # 以写的模式区打开新文件，不存在则创建
    new_f = open(new_file, 'w', encoding='utf-8')
    # 将文件内容全部读取出来
    content = old_f.read()
    # 把旧文件内容复制到新文件
    new_f.write(content)
    old_f.close()
    new_f.close()
    pass

# copyfile()

# 读取大文件
def copyBigFile():
    # 接收用户输入的用户名
    old_file = input('请输入文件名....')
    file_list = old_file.split('.')
    print(file_list)
    # 构造新的文件名.加上备份的后缀
    new_file = file_list[0]+'_备份.'+file_list[1]
    try:
        # 监视异常处理逻辑，防止内存泄漏
        with open(old_file, 'r', encoding='utf-8') as old_f, open(new_file, 'w', encoding='utf-8') as new_f:
            # 一次性读取1024字符
            while True:
                content = old_f.read(1024)
                new_f.write(content)
                if len(content) < 1024:
                    break
        pass
    except Exception as msg:
        print(msg)
    pass

copyBigFile()