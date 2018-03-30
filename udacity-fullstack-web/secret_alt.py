import os


location = r"D:\scharati\myProjects\github\learnings\udacity-fullstack-web\prank"

contents = os.listdir(location)

print(contents)

def rename_file(file_name):
    return file_name.translate(None,"0123456789")

for file in contents:
    renamed_file_name = rename_file(file)
    src_path = os.path.join(location,file)
    dest_path = os.path.join(location,renamed_file_name)
    os.rename(src_path,dest_path)