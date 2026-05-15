###task 1

def sum_of_digits(n):
    if n == 0:
        return 1
    return n + sum_of_digits(n - 1)
print(sum_of_digits(5))



###task 2

is_even = lambda n: n % 2 == 0

n = int(input("Enter number:"))

print(is_even(n))



###task 3

students = [
    ("Luka", 15, 85),
    ("Ana", 14, 92),
    ("Giorgi", 16, 78),
    ("Nino", 15, 95)
]

stundet_sorted = sorted(students, key=lambda x: (x[1], x[2]))
print(stundet_sorted)



###task 4

words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

sorted_words_length = sorted(words, key=lambda x: len(x))

print(sorted_words_length)



###5

words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

words_title = list(map(lambda x: x.title(), words))

print(words_title)



###task 6
numbers = [5, 12, 7, 18, 3, 24, 9]

filtered_numbers = list(filter(lambda x: x > 10 and x % 3 ==0, numbers))

print(filtered_numbers)
