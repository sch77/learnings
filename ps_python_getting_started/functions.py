students = []
students_titlecase = []

def get_students_titlecase():
    for student in students:
        student_name = student["name"].title()
        students_titlecase.append(student_name);
    return students_titlecase

def print_students_titlecase():
    all_students = get_students_titlecase()
    for name in all_students:
        print(name);

def add_student(name,student_id=332):
    student = {"name": name , "student_id":student_id}
    students.append(student)



def read_file():
    try:
        f = open("students.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("File could not be read");

def save_file(student):
    try:
        f = open("students.txt","a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("File could not be saved")


read_file();
print_students_titlecase()

isAddStudents = True;
while isAddStudents:
    if(input("Add more students ? Enter Y for Yes N for No: ") == "Y" ):
        student_name = input("Enter Student Name : ")
        student_id = input("Enter student ID : ")
        add_student(student_name,student_id)
        save_file(student_name)
    else:
        isAddStudents = False

