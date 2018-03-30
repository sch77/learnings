#
#
# content = "bangalore"
# list_content = list(content)
# mod_list = ""
#
# for c in list_content:
#     if c.isalpha():
#         print ("c is : " + c)
#         mod_list = mod_list + c
#
# print mod_list

import string

# dot_notation = "."
#
# dot_notation_list = list(dot_notation)
#
# print dot_notation_list
#
# if "." in  string.punctuation:
#     print "contains dot"

city = "34Bangalore"
mod_city = string.translate(city,None,"0123456789")
print(mod_city)

new_city = city.translate(None,"0123456789")
print("new")
print(new_city)