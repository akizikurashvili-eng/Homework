#task 1

python_1 = 50
print (type(python_1))
print (python_1)

python_2 = 'Snake'
print (type(python_2))
print (python_2)

python_3 = True
print (type(python_3))
print (python_3)

python_4 = 50.5
print (type(python_4))
print (python_4)



#task 2

name = input ('სახელი:')
bd = int (input('დაბადების წელი:'))
year = 2025
age = year - bd

greeting = f'გამარჯობა, ძვირფასო {name}! თქვენ მოცემულ მომენტში ხართ {age} წლის.'
print(greeting)



#task 3

#1/2
number = int(input('დაწერე ციფრი:'))
result = number % 2
print (bool(result)) #ლუწი & 0 = False; კენტი = True

#2/2
number = int(input ('შეიყვანე ციფრი:'))

print (bool(number))
#აქ ვერ შევძელი რაიმე მანიპულაციის მოფიქრება მხოლოდ bool ით
#დადებითი და უარყოფითი რიცხვები ორივე True-ს იძლევა.
