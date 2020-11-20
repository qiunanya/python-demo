# 序列操作
let = [1,2,3,0]
print(any(let))

# all() 除了0、空、False外都是true
print('all 判断', all(()), all([]), all([1, 2, False]), all([1, 2, 3]), all((1, 2, 3, 4)))

# any() 除了0、空、False外都是true, 函数有一个元素不为0、空、False的都为true
print('any 判断', any((2, 3, 4)), any(("", False, 0)))

# sorted() 函数对所有可迭代的对象进行排序操作, sort 用于list列表
li = [1, 2, 5, 4, 3]
li.sort()
print('sort 列表元素排序 ', li)

# sorted 排序 reverse=True 降序 reverse=False 升序
print('sorted 排序之前 {} '.format(li))
sorts = sorted(li, reverse=True)
print('sorted 排序之后 {}'.format(sorts))

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组
# ，然后返回由这些元组组成的的列表, 按照元素个数最少的组合并返回值
aa = zip([1, 2, 3],['a', 'b', 'c'])
print('zip 迭代 案例 ', aa, list(aa))