import os
import string

location = "D:\\scharati\\myProjects\\github\\learnings\\udacity-fullstack-web\\prank\\prank"

def file_name_for_rename(item_list):
    # print(item_list)
    mod_item_list = ""
    for c in item_list:
        # print("c is : " + str(c.isalpha()))
        if c.isalpha() or c in string.punctuation:
            mod_item_list = mod_item_list + c
    return mod_item_list


content = os.listdir(location)
# print content

for item in content:
    print("item is : " + item)
    print("modified item is : " + file_name_for_rename(list(item)))
    renamed_file_name = file_name_for_rename(list(item))
    src_path = location + "\\" + item
    tgt_path = location + "\\"+renamed_file_name
    print renamed_file_name
    if renamed_file_name != None:
        os.rename(src_path,tgt_path)






