my = ['张三', '李四', '网速5', '废话当时的佛海']
strings = '我是一个员工'
for i in my:
    print(i, len(i), len(my))
    pass


# end = '' 表示横排打印日志
for i in range(50, 70):
    if i % 2 == 0:
        print('%d是偶数' % i)
        pass
    else:
        print('%d是奇数' % i)
pass

# 使用跳出循环体 break
sum = 0
for i in range(1, 51):
    if sum > 100:
        print('循环到这里跳出了')
        break
        pass
    sum += i
    pass
print('sum = %d' % sum)

print('99 乘法表==========')
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d  " % (i, j, i*j), end='')
        pass
    print()
pass
