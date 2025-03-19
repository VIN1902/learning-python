class Form:
    def __init__(self, name, rollno):
        self.__name = name
        self.__rollno = rollno
    
    def get_name(self):
        return self.__name
    
    def get_rollno(self):
        return self.__rollno
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_rollno(self, new_rollno):
        self.__rollno = new_rollno

my_form = Form("Vikas", "22104039")
print(my_form.get_name())
print(my_form.get_rollno())
# print(my_form.__name) raises an error cause that private variable is only useable/meangiful inside the class.
my_form.set_name("Sakiv")
print(my_form.get_name())

# using '__' before a variable inside a class you can privatize it.