name_list = ["zhangsan","lisi","wangwu"]

# 1. 取值和索引
print(name_list[0])
print(name_list[1])
# 1.1 知道数据求索引下标
print(name_list.index("wangwu"))
# name_list.index("wwww")
# 2. 修改
name_list[1] = "李四"
# name_list[3] = "王小二"  # IndexError: list assignment index out of range
# 3. 增加
name_list.append("王小二")
name_list.insert(1,"1")
temp_name_list = [1,2,3]
name_list.extend(temp_name_list)
num_list = ["haode",1,3.14]
print(num_list)
# 4. 删除
name_list.pop()
name_list.pop(1)
del name_list[0]
name_list.remove("王小二")

name = "xxx"
del name
print(name)

print(name_list)