__author__ = "lfs"

name = "my \t name is {name}, i am {year} old"

#首字符大写
print(name.capitalize())

#包含的个数
print(name.count("a"))

#打印---name---
print(name.center(50, "-"))

#判断字符串结尾
print(name.endswith("fs"))

print(name.expandtabs(tabsize=30))

#字符串截取
print(name[name.find("name"):])

print(name.format(name='lfs', year=23))

print(name.format_map({'name':'lfs', 'year':12}))

#英文字符和数字
print(name.isalnum())

#纯英文
print(name.isalpha())

#是否是10进制
print(name.isdecimal())

#是否是整数
print(name.isdigit())

#是否是合法的标识符
print(name.isidentifier())

#是否只有数字
print(name.isnumeric())

#是否是空格
print(' a'.isspace())

#是否是每个首字符大写
print('My Name Is'.istitle())

#是否可以打印
print('My Name Is'.isprintable())
#是否是大写
print('My Name Is'.isupper())

print(','.join(['1', '2', '3']))

#全部小写
print('My Name Is'.lower())

#全部大写
print('My Name Is'.upper())

#去左边回车
print('\nMy Name Is'.lstrip())

#去右边回车
print('\nMy Name Is'.rsplit())

#去回车
print('\nMy Name Is\n'.strip())

p = str.maketrans("abcdef", '123456')

print("lfs".translate(p))

print('alex li'.replace('l', 'L', 1))

print('aleex lie'.rfind('e'))

print('aleex lie'.split())
print('aleex \nlie'.splitlines())
print('aleex Lie'.swapcase())
print('aleex lie'.title())
print('aleex lie'.zfill(30))
