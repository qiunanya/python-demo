# set 集合，主要用于去重
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4}
set1.add('python')
print(type(set1), set1)
set1.remove('python')
# set1.remove('qiu')
# set1.clear()
# set1.update('邱南亚')
print(set1)

print('set1 和 set2 差集', set1.difference(set2))
print('set1 和 set2 交集', set1.intersection(set2))
print('set1 和 set2 并集', set1.union(set2))
print('set1 和 set2 交集', set1 | set2)
set1.pop()
print('pop 取出元素', set1)
set1.discard(2)
print('discard 移除指定元素 2', set1)

set1.update(set2)
sorted(set1, reverse=False)
print('update 更新set1结果 ', set1)


