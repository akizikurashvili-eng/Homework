# #task 1

def find_min_max(*args):
    smallest = f' მინიმალური ციფრია: {min(args)}'
    largest = f' მაქსიმალური ციფრია: {max(args)}'
    return smallest, largest

result = find_min_max (2, 5, 6, 19, 11, 9, 21)
print(result)



# #task 2

def calculator(*args, operations):

    if operations == "sum":

        return sum(args)

    elif operations == "min":
        return min(args)

    elif operations == "max":
        return max(args)

    elif operations == "mult":

        result = 1

        for num in args:
            result *= num

        return result

    else:
        return "wrong operation"


numbers = input('შეიყვანეთ ციფრები: ')

numbers_list = numbers.split()

numbers_list = [int(num) for num in numbers_list]

oper = input(
    'შეიყვანე მოქმედება (sum, min, max, mult): '
).lower().strip()

final_result = calculator(*numbers_list, operations=oper)

print(final_result)




#task 3

def format_user (firs_name, last_name, **kwargs):
    print (f' "სახელი:" {firs_name}, "გვარი:" {last_name}, {kwargs}')

name = input ("შეიყვანეთ სახელი:").title().lstrip().rstrip(" ")
lname = input ("შეიყვანეთ გვარი:").title().strip()
job = input ("სამსახური:").title().strip()
age = int (input ("ასაკი:"))

format_user(name, lname, სამსახური=job, ასაკი=age)



#task 4

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        quotient = a // b
        remainder = a % b
        return f' "მთელი ნაწილი:" {quotient}, "ნაშთი:" {remainder}'

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

final_result = safe_divide(num1, num2)
print(final_result)











