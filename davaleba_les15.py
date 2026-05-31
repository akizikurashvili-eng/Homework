### Task 1 ძაღლის კლასი

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print (f'{self.name} says Woof')
    def info(self):
        print (f'{self.name} is {self.age} years old')

dog_1 = Dog('Ckifo', '4')
dog_2 = Dog('Dobermana', '5')
dog_3 = Dog('Artura Arutinovi', '6')

dog_1.info()
dog_2.info()
dog_3.info()
dog_1.bark()
dog_2.bark()



# #### Task 2 მართკუთხედის კლასი


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

    def perimeter(self):

        return 2 * (self.width + self.height)

    def is_square(self):

        return self.width == self.height


rect1 = Rectangle(5, 10)

print(f"ფართობი: {rect1.area()}")
print(f"პერიმეტრი: {rect1.perimeter()}")
print(f"კვადრატია?: {rect1.is_square()}")
print("-" * 20)

rect2 = Rectangle(6, 6)

print(f"ფართობი: {rect2.area()}")
print(f"კვადრატია?: {rect2.is_square()}")



### Task 3 საბანკო ანგარიში


class Bank:
    bank_name = 'Step Bank'

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print (f'{self.owner} თქვენ ბალანსზე დაამატეთ {amount} ლარი და თქვენი ბალანსი შეადგენს {self.balance} ლარს')

    def withdraw(self, amount):
        if amount > self.balance:
            print (f'{self.owner} თქვენს ანგარიშზე არასაკმარისი თანხაა')
        else:
            self.balance -= amount
            print(f' {self.owner} თქვენ ბალანსიდან გაიტანეთ {amount} ლარი და თქვენი ბალანსი შეადგენს {self.balance} ლარს')


    def show_balance(self):
        print(f' გამარჯობა {self.owner}, თქვენი ბალანსი {self.bank_name}-ში არის {self.balance} ლარი')

custumer_1 = Bank('Lado', 1500)
custumer_2 = Bank('Bondo', 1000)

custumer_1.deposit(100)
custumer_1.withdraw(500)
custumer_1.show_balance()

custumer_2.deposit(100)
custumer_2.withdraw(500)
custumer_2.show_balance()

custumer_1.withdraw(5000)
custumer_1.show_balance()



#### Task 4


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Classroom:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)

    def average(self):

        if not self.students:
            return 0.0
        total_grade = sum(student.grade for student in self.students)
        avg = total_grade / len(self.students)
        return round(avg, 2)


    def top_student(self):
        if not self.students:
            return "No students in the classroom"

        best_student = max(self.students, key=lambda s: s.grade)
        return best_student.name


student1 = Student("Bondo", 8)
student2 = Student("Zaali", 9)
student3 = Student("Mzevinari", 10)
student4 = Student("Nodari", 7)

my_class = Classroom()

my_class.add_student(student1)
my_class.add_student(student2)
my_class.add_student(student3)
my_class.add_student(student4)



print("="*40)
print ("კლასის საშუალო ქულა", my_class.average())
print("="*40)

print("="*40)
print("საუკეთესო მოსწავლე კლასში", my_class.top_student())
print("="*40)



