#task 1

age = int (input ('გთხოვთ შეიყვანეთ თქვენი ასაკი:'))

if (age <= 12) :
    print ('ბავშვი')
elif (age <= 19) :
    print ('თინეიჯერი')
elif (age <= 64) :
    print ('ზრდასრული')
else:
    print ('უფროსი')


#task 2

score = float(input("შეიყვანეთ თვენი ქულა:"))
att = float(input("შეიყვანეთ თქვენი დასწრების პროცენტულობა:"))

if score > 65 and att > 75:
    print ('ჩააბარა')
else:
    print ('ვერ ჩააბარა')


# task 3

student = input ("ხართ სტუდენტი? Yes/No:")
member = input ('ხართ წევრი? Yes/No:')


if student == 'Yes'and member == 'Yes':
    print ("თქვენ გაქვთ დიდი ფასდაკლება")
elif student == 'Yes'or member == 'Yes':
    print ("თქვენ გაქვთ ფასდაკლება")
else:
    print ("თქვენ არ გაქვთ ფასდაკლება")


#task 4

username = input('გთხოვთ შეიყვანოთ username:')

num1 = 3
num2 = 20

if (num1 < int(len(username)) < num2 ) and username.isalnum() == True:
    print ("username სწორია")
else:
    print ("username არასწორია")