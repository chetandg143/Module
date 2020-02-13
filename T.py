# program to calculator , marks card and Student record

print(" ****** WELCOME TO TASK *********")

class Calculator:
    def add(a, b):
        return a + b
    def sub(a,b):
            return a - b
    def mul(a , b):
            return a * b
    def div(a , b):
        return a/b
    def cal():
        print("Select operation to be performed")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")

        choice = input("Enter choice(1/2/3/4): ")

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", Calculator.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Calculator.sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Calculator.mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Calculator.div(num1, num2))
        else:
            print("Invalid input/n")


class Markscard:
   # sub =(int(input("enter the number of subjects :")))
        def perc():

            print("************* MARKS CARD SHEET *****************\n")
            print("********enter the marks of subjects********\n")
            sub1 = (int(input(" enter kannada  marks :")))
            sub2 = (int(input(" enter English  marks :")))
            sub3 = (int(input(" enter Science  marks :")))
            sub4 = (int(input("enter mathematics  marks :")))
            sub5 = (int(input("enter Social science  marks :")))
            sub6 = (int(input("enter Hindi  marks :")))

            average = int(sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 6
            print("Student % scored :", average)

            if (average > 90):
                     print(" Congratulations!! scored Grade: A+")

            elif (average >= 80 or average < 90):
                     print(" Congratulations!! scored Grade: A")

            elif (average >= 70 or average < 80):
                     print("Congratulations!! scored Grade: B+")

            elif(average >= 60 or average < 70):
                     print("Congratulations!! scored Grade: B")

            elif (average >= 50 or average < 60):
                     print("Congratulations!! scored Grade: C")

            elif (average >= 40 or average < 50):
                     print("Congratulations!! scored Grade: D")

            else:
                     print("Congratulations!! scored Grade: F")



class Student:
        def __init__(self, name, rollno,gender,age):
                self.sname = name
                self.rollno = rollno
                self.gender = gender
                self.age = age
        def  display(ob):
                dict = {"sname":ob.name, "sno ": ob.rollno, "gender": ob.gender, "sage": ob.age}
                for x, y in dict.items():
                    print(x, " : ", y)

        def display():
            print("######## Student Record's 2020 #############\n")
            name = str(input("enter name of student :"))
            rollno =int(input("enter the roll number :"))
            gender = (str(input("enter gender (M\F) :")))
            age = (int(input("enter the age :")))
            ob = Student(name,rollno,gender,age)
            ob.display()

print("enter 1 for Calculator ")
print("enter 2 for Markscard ")
print("enter 3 for Student Record")
option = input("enter the option :")
if option == '1':
    Calculator.cal()
elif option == '2':
    Markscard.perc()
elif option == '3':
    Student.display()















