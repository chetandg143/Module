class Student:
    def __init__(self, name, rollno, gender, age):
        self.name = name
        self.rollno = rollno
        self.gender = gender
        self.age = age

    def display(ob):
        dict = {"sname": ob.name, "sno ": ob.rollno, "gender": ob.gender, "sage": ob.age }
        for x, y in dict.items():
                 print(x, " : ", y)
name = str(input("enter name of student :"))
rollno = int(input("enter the roll number :"))
gender = (str(input("enter gender (M\F) :")))
age = (int(input("enter the age :")))

s1 = Student(name, rollno, gender, age)
s1.display()

