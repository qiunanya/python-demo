try:
    # 捕获错误
    print(b)
    li = [1,4,7]
    print(li[10])
    pass
except NameError as msg:
    # 捕获到的错误，才会在这里执行
    print(msg)
    pass
except IndexError as msg:
    print(msg)
    pass

# 全部异常捕获类型
except Exception as result:
    # 捕获到的错误，才会在这里执行
    print(result)
    pass

print('山东山东分行的')