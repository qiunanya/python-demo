# 通过python 的 pymysql桥梁 测试连接数据库
from pymysql import *
# 连接数据库
conn = connect(host="39.106.29.92", user="root", password="123456", database="test", port=int(3306), charset="utf8")
# 创建一个游标对象 可以利用这个对象进行数据库的操作

try:
    opt_sql = conn.cursor()
    sql: str = 'insert into permission(permission_id, permission_name, permission_url, permission_comment) values ("sdhsf46846sdf4444s", "add", "dhhddhhdh///", "新增员工")'
    opt_sql.execute(sql)
    conn.commit()
    # opt_sql.execute('select * from permission')
    # result = opt_sql.fetchall()
    # for item in result:
    #     print('角色标识{0} 角色名称 {1} 菜单路径{2}'.format(item[1], item[3], item[2]))
    #     pass
    # print(type(result))
    print(opt_sql)
    print('success')
except Exception as msg:
    print(msg)
finally:
    opt_sql.close()
    conn.close()
    print('结束')