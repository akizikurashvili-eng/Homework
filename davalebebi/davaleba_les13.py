### task 1 ლისტიდან უსაფრთხო წვდომა
from asyncio import exceptions


def safe_get(lst, index):

    try:
        item = lst[index]

    except TypeError as e:
        print(e)
        print("Index must be an integer")
    except IndexError as e:
        print(e)
        print("There is no item with this index")
    else:
        print("All good")
        return item
    finally:
        print("Finished")

lst = ['car', 'plane', 'train', 'boat', 'bicycle']

result = safe_get(lst, 3)
print(result)

result = safe_get(lst, 8)
print(result)

result = safe_get(lst, 'car')
print(result)

###### kitxva: None ratom micers "finished" - is shemdeg?




### task 2 დიქტიდან უსაფრთხო წვდომა

def safe_get_value(dictionary, key):
    try:
        value = dictionary[key]
    except KeyError as e:
        print(e)
        print("There is no item with this key")
    except Exception as e:
        print(e)

    else:
        print("All good")
        return value
    finally:
        print("Finished")

class_a = {"Ana" : "A",
"Bob" : "F",
"Carl" : "B",
"Bondo":"A+"
}

result = safe_get_value(class_a, "Ana")
print(result)

result = safe_get_value(class_a, "Beno")
print(result)

result = safe_get_value('Carl', 'Ana')
print(result) #Ecxeption -ma arascori erroris tipi momca. Exceptioni arazustad aidentificirebs erorebs?




### Task 3 რიცხვის კვადრატი

try:
    num = int(input('Enter a number: '))
    result = num ** 2
except ValueError as e:
    print(e)
    print('აუცილებელია შეიყვანოთ ციფრი')
except Exception as e:
    print(e)
    print('დაფიქსირდა შეცდომა')
else:
    print(result)
finally:
    print('ოპერაცია დასრულებულია')