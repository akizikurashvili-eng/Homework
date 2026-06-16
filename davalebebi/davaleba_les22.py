### წიგნების ბიბლიოთეკის მართვის სისტემა
### JSON

import json
import os
from dataclasses import asdict, dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    available: bool


def save_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump([asdict(b) for b in books], f, ensure_ascii=False, indent=2)


def load_books():
    if os.path.exists("books.json"):
        with open("books.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**item) for item in data]
    return []


def main():
    books = load_books()

    while True:
        print("\n--- წიგნების მართვის სისტემა ---")
        print("1. წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა სახელით")
        print("4. წიგნის გატანა")
        print("5. წიგნის დაბრუნება")
        print("6. სტატისტიკა")
        print("7. მონაცემების შენახვა")
        print("8. გამოსვლა")

        choice = input("\nაირჩიეთ მოქმედება (1-8): ").strip()

        if choice == "1":
            title = input("შეიყვანე სახელი: ").strip()
            author = input("შეიყვანე ავტორი: ").strip()
            try:
                year = int(input("შეიყვანე წელი: "))
            except ValueError:
                print("შეცდომა: წელი უნდა იყოს რიცხვი!")
                continue

            new_id = max((b.id for b in books), default=0) + 1
            books.append(Book(new_id, title, author, year, True))
            print("✅ წიგნი დაემატა!")

        elif choice == "2":
            for b in books:
                status = "ხელმისაწვდომი" if b.available else "გაცემული"
                print(f"ID: {b.id} | {b.title} | {b.author} | {b.year} | {status}")

        elif choice == "3":
            search = input("შეიყვანეთ საძიებო სიტყვა: ").strip().lower()
            for b in [b for b in books if search in b.title.lower()]:
                status = "ხელმისაწვდომი" if b.available else "გაცემული"
                print(f"ID: {b.id} | {b.title} | {b.author} | {b.year} | {status}")

        elif choice == "4":
            try:
                book_id = int(input("შეიყვანეთ ID გასატანად: "))
                book = next((b for b in books if b.id == book_id), None)
                if book and book.available:
                    book.available = False
                    print("✅ წიგნი გაიცა!")
                else:
                    print("❌ წიგნი ვერ მოიძებნა ან უკვე გაცემულია!")
            except ValueError:
                print("შეცდომა: ID უნდა იყოს რიცხვი!")

        elif choice == "5":
            try:
                book_id = int(input("შეიყვანეთ ID დასაბრუნებლად: "))
                book = next((b for b in books if b.id == book_id), None)
                if book:
                    book.available = True
                    print("✅ წიგნი დაბრუნდა!")
                else:
                    print("❌ წიგნი ვერ მოიძებნა!")
            except ValueError:
                print("შეცდომა: ID უნდა იყოს რიცხვი!")

        elif choice == "6":
            total = len(books)
            avail = sum(1 for b in books if b.available)
            print(f"სულ წიგნები: {total}")
            print(f"ხელმისაწვდომი: {avail}")
            print(f"გაცემული: {total - avail}")

        elif choice == "7":
            save_books(books)
            print("💾 მონაცემები შენახულია!")

        elif choice == "8":
            save_books(books)
            break


if __name__ == "__main__":
    main()