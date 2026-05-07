# #task1
for a in range(10):
    for b in range(10):
        print(f'{a}+{b}={a + b}' , end='    ')
    print()


# #task2
numbers = [18, 5, 44, 32, 3, 15]

max_num = numbers[0]
min_num = numbers[0]


for num in numbers:
    if num > max_num:
        max_num = num

    if num < min_num:
        min_num = num

print("მაქსიმალური რიცხვი:", max_num)
print("მინიმალური რიცხვი:", min_num)


#task3


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in list if number % 2 == 0]
odd_numbers = [number for number in list if number % 2 != 0]
print('ლუწი რიცხვების ლისტიდან:', even_numbers)
print('კენტი რიცხვები ლისტიდან:', odd_numbers)


#task4

list = [1,2,3,4,5,6,7,8,9,10]
tuple_list = tuple(list)
print(list)
print(tuple_list)


#task 5

list = [1, 2, 2, 4, 5, 6, 6, 7, 3, 4, 5, 8, 9, 10]

un_number = []

for num in list:
    if num not in un_number:
        un_number.append(num)
        un_number.sort()

print ('უნიკალური რიცხვები:', un_number)
print('თავდაპირველი ლისტი:', list)


# ვეცადე აქ ქომრეჰენშენითაც მექნა მაგრამ ავირიე.
