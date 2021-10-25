# 格式化输出
str = "学生管理系统"
print('{0:@^30}'.format(str))
print('{0:*<30}'.format(str))
print('{0:*>30}'.format(str))

# 反转单词输出
str_input = input("输入一段英文:")
print("原句子：" + str_input)
str_tmp = ""
str_list = str_input.split(" ")
str_new = list(reversed(str_list))
for i in str_new:
    str_tmp = str_tmp + i + " "
print(str_tmp)
