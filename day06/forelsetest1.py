# for num in [1, 2, 3, 4, 5, 6]:
#     print(num)
#     if num == 5:
#         break
# else:
#     print("else")
# print("for done")

students_info = [
    {"name": "小美", "sex":"nv"},
    {"name": "张三", "sex":"nan"}
]
find_name = "张三"
for i in students_info:
    if i["name"] == find_name:
        print("找到了！")
        break
else:
    print("没找到！")
print("for done")