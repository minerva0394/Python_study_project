def test(str):
    final_str = ""
    if str.isdigit():
        print(str)
    elif str.islower():
        print(str.upper())
    elif str.isupper():
        print(str.lower())
    else:
        for i in str:
            if i == " ":
                final_str += " "
            if i.isupper():
                final_str += i.lower()
            elif i.islower():
                final_str += i.upper()
            elif i.isdigit():
                i = i
                final_str += i
    return final_str


if __name__ == '__main__':
    str = input("输入字符串:")
    test(str)
