#task 1

n =int(input("შეიყვანე დადებითი მთელი რიცხვი, რომელიც მეტია 1ზე:"))
while n > 1 :
    print (n)
    n -= 1
print ("liftoff")




#task 2

total = 0
number = 0
while True:
    number = int(input('Enter a number: '))
    if number == 0:
        break
    total += number
    print(total)




#task 3

secret_number = 7
number = 0
while number != secret_number:
    number = int(input("შეიყვანეთ მთელი რიცხვი:"))
    if number < secret_number:
        print("to low")
    if number > secret_number:
        print("to high")
print("Correct!")



#task 4

#1/4
for number in range(9):
    print(number)

#2/4
for number in range(5, 15):
    print(number)

#3/4
for number in range(2, 20):
    if number % 2 == 1:
        continue
    print(number)

#4/4
for number in range(10, 1, -1):
    print(number)
