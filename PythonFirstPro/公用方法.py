# 公用方法操作
strA = "人生苦短"
strB = '我 用 python'
# 字符串合并
print('拼接 %s' % (strA+strB))

# 列表合并
listA = list(range(6))  
listB = list(range(4))
print('列表合并 %s' % (listA + listB))

# 复制
print('%s ' % strA*4)

# in 对象是否存在 结果是一个bool值
# 字符串
print('我' in strA)
print('人' in strA)
# 列表
print('列表里是否由45 %s' % 45 in listA)