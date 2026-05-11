# # #task 1

transports = ['car', 'train', 'plane', 'car', 'tram', 'plane', 'car', 'train']

transport_dict = {}

for transport in transports:
    if transport in transport_dict:
        transport_dict[transport] += 1
    else:
        transport_dict[transport] = 1

print(transport_dict)




# # #task 2

dict1 = {
    "name": "Gio",
    "age": 20,
    "city": "Tbilisi"
}
dict2 = {
    "name": "Nika",
    "age": 25,
    "country": "Georgia"
}

new_dict = {}
for key in dict1:
    if key in dict2:
        new_dict[key] = [dict1[key], dict2[key]]
    else:
        new_dict[key] = dict1[key]
for key in dict2:

    if key not in new_dict:
        new_dict[key] = dict2[key]

print(new_dict)




# # #task 3

my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
reversed_dict = {}

for key in my_dict:
    reversed_dict[my_dict[key]] = key

print(reversed_dict)



# # #task 4

films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}

films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}

common_films = films1 & films2
only_films1 = films1 - films2
only_films2 = films2 - films1
all_films = films1 | films2

print("საერთო ფილმები:", common_films)
print("მხოლოდ films1-ში:", only_films1)
print("მხოლოდ films2-ში:", only_films2)
print("ყველა უნიკალური ფილმი:", all_films)




#task 5 (es ver gavige da ai daxmarebit gavakete)

import json

with open("info.json", "r", encoding="utf-8") as file:
    data = json.load(file)

students = data["students"]

# 1
for student in students:
    print(student["name"], "-", student["average_score"])

# 2
best_student = max(students, key=lambda s: s["average_score"])
print(best_student["name"])

# 3
for student in students:
    if student["attendance"] > 90:
        print(student["name"])

# 4
grade_count = {}

for student in students:
    grade = student["grade"]

    if grade in grade_count:
        grade_count[grade] += 1
    else:
        grade_count[grade] = 1

largest_grade = max(grade_count, key=grade_count.get)

print(largest_grade)

# 5
for student in students:
    if "Programming" in student["subjects"]:
        print(student["name"])

# 6
total_attendance = 0

for student in students:
    total_attendance += student["attendance"]

average_attendance = total_attendance / len(students)

print(average_attendance)

# 7
subjects_count = {}

for student in students:
    subjects_count[student["name"]] = len(student["subjects"])

print(subjects_count)

# 8
most_active = max(
    students,
    key=lambda s: len(s["activities"])
)

print(most_active["name"])
