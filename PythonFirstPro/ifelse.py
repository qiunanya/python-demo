# 单分支结构
# score = int(input('请输入分数:'))
# if 100 >= score >= 90:
#     print('A'+'很优秀')
# elif 90 > score >=80:
#     print('B')
# elif 80 > score >= 60:
#     print('C')
# elif 60 >score >= 0:
#     print('不及格 D')
# else:
#     print('输入错误！')


# pass 表示空语句，结束，跳出之意
score = 80
# 测试
if score > 60:
    print('你的成绩及格了')
    pass
else:
    print('成绩不合格')
    pass

# 三元表达式

numer = 5

value = 8 if 5 > 3 else 15

print("三元表达式值 =》", value)