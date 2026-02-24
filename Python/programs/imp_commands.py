#sep parameter to control separators. by default its single space ' '

print('India', 'UK', 'Singapore', 'Hongkong', 'Dubai', 'Germany', 'Austria')
print('India', 'UK', 'Singapore', 'Hongkong', 'Dubai', 'Germany', 'Austria', sep='/')


#check if there is any reserved keyword - there are 33 reserved keywords in python
import keyword
print(keyword.kwlist)

string = 'This is Python'
multiline_str = """this is multiline string with more information to print especially if string is of more than 1 line"""
unicode = u"\U0001f600 \U0001f606 \U0001f923 "
raw_str = r"raw \n string"
print(string)
print(multiline_str)
print(unicode)
print(raw_str)
