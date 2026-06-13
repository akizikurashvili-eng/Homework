import csv
import os
from datetime import datetime
import pandas as pd

product_file = 'products.csv'
data_file = 'data.txt'

def initialization_file():
    if not os.path.exists(product_file):
        with open(product_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Product Name', 'Price', 'Stocks'])

def log_action (username, action, extra_info=''):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_text = f"[{current_time}] {username} || {action}"
    if extra_info:
        log_text += f" | {extra_info}"
    with open(data_file, 'a', newline='', encoding='utf-8') as file:
        file.write(log_text + '\n')

def generate_next_id():
    max_id = 0
    if os.path.exists(product_file):
        with open(product_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    current_id = int(row['ID'])
                    if current_id > max_id:
                        max_id = current_id
                except ValueError:
                    continue
    return max_id + 1

def show_all_products(username):
    print ('\n ------Product List------')
    df = pd.read_csv(product_file, index_col='ID', na_values=['-', 'N/A'], dtype={'price':float, 'stocks':int})
    print(df)

    log_action(username, 'Viewed all products')

def find_product_by_id(username):
    product_id = int(input("Enter product ID: ").strip())


    df = pd.read_csv(product_file, index_col='ID', na_values=['-', 'N/A'], dtype={'price': float, 'stocks': int})
    find_product = df.loc[product_id]
    print(find_product)
    log_action(username, 'GET_PRODUCT', f'PRODUCT_ID={product_id}')

def add_product(username):
    print("------Add product------")
    product_name = input("Enter product name: ").strip()

    try:
        price = float(input("Enter product price: "))
    except ValueError:
        print("Invalid input for price")
        print('Product not added')
        return
    try:
        stocks = int(input("Enter product stocks: "))
    except ValueError:
        print("Invalid input for stock")
        print('Product not added')
        return

    next_id = generate_next_id()
    new_product = pd.DataFrame([{
        'ID': next_id,
        'Product Name': product_name,
        'Price': price,
        'Stocks': stocks
    }])
    new_product.to_csv(product_file, index=False, mode='a', header=False, encoding='utf-8')

    print(f'Product {product_name} added with ID {next_id}')
    log_action(username, 'ADD_PRODUCT', f'NAME={product_name}')

def remove_product(username):
    print("------Remove product------")
    product_id = input("Enter product ID to remove: ").strip()
    updated_products = []
    found = False
    with open(product_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            if row['ID'] == product_id:
                found = True
            else:
                updated_products.append(row)

    if found:
        with open(product_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames = headers)
            writer.writeheader()
            writer.writerows(updated_products)

        print(f'Product {product_id} removed')
    else:
        print(f'Product {product_id} not found')

    log_action(username, 'DELETE_REMOVED', f'PRODUCT_ID={product_id}')


def main():
    initialization_file()

    print('Welcome to Product Manager System')
    username = input("Enter username: ")
    if not username:
        username = "Unknown User"

    while True:
        print("\n==================== MENU ====================")
        print("1. Show all products")
        print("2. Get product by id")
        print("3. Add product")
        print("4. Delete product")
        print("5. Exit")
        print("==============================================")

        try:
            choice = int(input("Enter your choice(1-5): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            show_all_products(username)
        elif choice == 2:
            find_product_by_id(username)
        elif choice == 3:
            add_product(username)
        elif choice == 4:
            remove_product(username)
        elif choice == 5:
            print(f"Goodbye, {username}!")
            log_action(username, "EXIT_PROGRAM")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()






