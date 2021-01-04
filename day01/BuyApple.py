in_price = input("请输入苹果单价：")
in_nums = input("请输入苹果数量：")
price = float(in_price)
nums = int(in_nums)
cost = price * nums
print("总价为：%.02f\n单价为：%.02f\n数量为：%04d\n" % (cost,price,nums))
