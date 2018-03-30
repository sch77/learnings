class Parent():
    def __init__(self, last_name, eye_color):
        print("calling Parent constructor")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("calling show_info from Parent")
        print(self.last_name)
        print(self.eye_color)


class Child(Parent):

    def __init__(self,last_name,eye_color,number_of_toys):
        print("calling Child constructor")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys
    
    def show_info(self):
        print("calling show_info Child")
        print(self.last_name)
        print(self.eye_color)
        print(self.number_of_toys)

