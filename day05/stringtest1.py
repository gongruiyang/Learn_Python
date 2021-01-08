# count函数
s ="hello world!"
print(s.count('o'))

# 判断整数函数
s = "一千零一"
print(s.isdigit())      # false
print(s.isnumeric())    # true
print(s.isdecimal())    # false

# 判断开头函数
s = "hello world!"
print(s.startswith("hello"))    # true
print(s.endswith("d!"))         # true

# find函数
s = "hello world!"
print(s.find("llo",0,len(s)))          # 2
print(s.find("abc"))          # -1

# replace函数
s = "hello world!"
s_new = s.replace("hello","python")
print(s_new)                        # python world!
print(s)                            # hello world!

# 对齐函数
poem = ["1", "23", "456", "789"]
for str in poem:
    print(str.rjust(15,'*'))

# 取出空格函数
s = "\t 111 11  1 1 1 \t\n"
s_new = s.strip()
print(s_new)

# 按特定字符分割函数
s = "1234.888"
s_list = s.split('.')
for i in s_list:
    print(i)

# 按特定字符拼接字符串函数
s = "1234\n\t888\n\t999\n   000\t"
s_list = s.split()
s_new = ".".join(s_list)
print(s_new)

# 字符串切片
s = "python"
print(s[1:6])
print(s[0:1])
print(s[-1:])
print(s[len(s)-1:len(s)])
print(s[::-1])
print(max(s))
print(min(s))

list1 = [1, 2, 3] * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(list1)
tuple1 = (1, 2, 3) * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(tuple1)
s = "hello" * 3     # hellohellohello
print(s)
list1.extend([[1, 2, 3], [3, 3, 3]])    # [1, 2, 3, 1, 2, 3, 1, 2, 3, [1, 2, 3], [3, 3, 3]]
print(list1)