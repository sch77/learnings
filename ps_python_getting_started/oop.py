class Student:
    school_name= "AECS Magnolia Maaruti Public School"
    def __init__(self,name,id):
        self.name = name;
        self.id = id
    def __str__(self):
        return "<" + "name: " + self.name + "  id: " + str(self.id)+">"
    def get_name(self):
        return self.name

myStudent = Student("Shailesh", 123)
print(myStudent)

print("name is:  " + myStudent.get_name())
print("static reference: " + Student.school_name)
print("statid reference also via instance", myStudent.school_name)