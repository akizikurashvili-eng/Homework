#task 1 დავითვალოთ ფაილიდან, სიტყვები, სტრიქონები, სიმბოლოები.


def analyze_text(f):
    len_symbol = len(f)
    len_word = len(f.split())
    len_lines = len(f.splitlines())
    print(f"სიმბოლოების რაოდენობა ფაილში არის: {len_symbol}")
    print(f"სიტყვების რაოდენობა ფაილში არის: {len_word}")
    print(f"ხაზების რაოდენობა ფაილში არის: {len_lines}")


try:
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    analyze_text(data)

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(e)



# #task 2 ჩანაწერების ჟურნალი

def journal_book (f):
    print ('ჩანაწერების ჟურნალი გააქტიურებულია')
    print ('ჟურნალიდან გამოსასვლელად შეიყვანეთ - "exit"')

    while True:
        type_info = input ('შეიყვანეთ ინფორმაცია:')
        if type_info.strip().lower() == 'exit':
            print ("თქვენ გამოხვედით ჟურნალიდან")
            print ("ყველა მანამდე შეყვანილი ინფორმაცია შენახულია")
            break

        with open ('journal.txt', 'a', encoding='utf-8') as file:
            file.write(type_info + '\n')

journal_book('journal.txt')



#task 3 ფილტრი
import csv


def min_price_filter():
    try:
        min_price = float(input("შეიყვანეთ მინიმალური ფასი: "))
    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვი (მაგ: 20, 20.5 და ა.შ)")
        return

    try:

        with open('products.csv', 'r', encoding='utf-8') as infile, \
                open('filtered_products.csv', 'w', encoding='utf-8', newline='') as outfile:

            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

            writer.writeheader()
            counter = 0

            for row in reader:
                row_price = float(row['price'])

                if row_price > min_price:
                    writer.writerow(row)
                    counter += 1


            print(f"ფილტრაცია წარმატებით დასრულდა! ახალ ფაილში გადავიდა {counter} პროდუქტი.")

    except FileNotFoundError:
        print("შეცდომა: ფაილი 'products.csv' ვერ მოიძებნა. დარწმუნდი, რომ კოდი და ფაილი ერთ საქაღალდეშია.")
    except KeyError:
        print("შეცდომა: ფაილში სვეტი სახელით 'price' ვერ მოიძებნა. შეამოწმე სვეტის სახელი ფაილში!")
    except Exception as e:
        print(f"მოხდა გაუთვალისწინებელი შეცდომა: {e}")


min_price_filter()




### TASK 4

import csv

try:
    with open ('contacts.csv', 'r') as contact_file:
        reader = csv.DictReader(contact_file)
        data = list(reader)
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(e)


# def all_contacts (f):
#
#     for contacts in data:
#         print(contacts['name'])

def add_contacts (f):
    name_1 = input('შეიყვანე კონტაქტის სახელი:').strip().title()
    tel = input('შეიყვანე კონტაქტის ტელეფონი:')
    em = input('შეიყვანე კონტაქტის ელ-ფოსტა:')

    with open ('contacts.csv', 'r+', newline='') as file:
        headers = [name_1, tel, em]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()


def find_contacts (f):
    try:
        name_to_find = input ('შეიყვანეთ საძიებო სახელი ლათინური ასოებით:').strip().title()
        if name_to_find in data['name']:
            print(f'{name_to_find} არის სიაში')
    except TypeError:
        print('შეიყვანეთ სახელი სწორად')


























