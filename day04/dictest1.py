ID_info_dic = {"姓名：":"张三", "身高：":1.75, "体重：":77.5,"年龄：":18}
print(ID_info_dic)
for info in ID_info_dic:
    print(info, end="")
    print(ID_info_dic.get(info))