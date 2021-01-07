# info_dic = {"name": "小明"}
# print(info_dic["name"])

# info_dic["name"] = 18
# info_dic["sex"] = 1
# print(info_dic)

# info_dic.pop("name")
# print(info_dic)

# info_dic = {"name":"mike","weight":77.5,"height":1.75}
# print(len(info_dic))
#
# temp_dic = {"sex" : 0}
# info_dic.update(temp_dic)
# print(info_dic)

# info_dic = {"name" : "Mike", "weight":77.5}
# temp_info_dic = {"height":180}
# info_dic.update(temp_info_dic)
# info_dic.clear()
# print(info_dic)

info_dic = {"name" : "Mike", "weight":77.5}
for key in info_dic:
    print("%s : %s" % (key, info_dic[key]))