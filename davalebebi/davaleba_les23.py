
import requests
from pydantic import BaseModel, ValidationError
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = "https://crudcrud.com/api/0ba720cb1b6744469087f5f718a47445"
TIMEOUT_LIMIT = 5


class Recipe(BaseModel):
    name: str
    cuisine: str
    time_minutes: str


recipes = [
    {"name": "Khachapuri", "cuisine": "Georgian", "time_minutes": "30"},
    {"name": "Khinkali", "cuisine": "Georgian", "time_minutes": "60"},
    {"name": "Mtsvadi", "cuisine": "Georgian", "time_minutes": "45"}
]

try:

    print("--- რეცეპტების დამატება (POST) ---")
    created_ids = []

    for recipe in recipes:
        response = requests.post(f'{BASE_URL}/recipes', json=recipe, timeout=TIMEOUT_LIMIT)
        response.raise_for_status()
        res_data = response.json()
        created_ids.append(res_data["_id"])
        print(f"დაემატა: {res_data['name']}, სტატუსი: {response.status_code}")


    print("\n--- ყველა რეცეპტის წაკითხვა (GET) ---")
    response = requests.get(f'{BASE_URL}/recipes', timeout=TIMEOUT_LIMIT)
    response.raise_for_status()
    data = response.json()
    for recipe_item in data:
        print(f"სახელი: {recipe_item['name']} | დრო: {recipe_item['time_minutes']}")
    print("-" * 20)


    real_id_khinkali = created_ids[1]
    real_id_mtsvadi = created_ids[2]


    print(f"\n--- კონკრეტული რეცეპტის წაკითხვა ID-ით ({real_id_khinkali}) ---")
    response = requests.get(f'{BASE_URL}/recipes/{real_id_khinkali}', timeout=TIMEOUT_LIMIT)
    response.raise_for_status()
    print("ერთი რეცეპტის მონაცემები:", response.json())


    print(f"\n--- რეცეპტის განახლება (PUT) კონკრეტულ ID-ზე: {real_id_khinkali} ---")
    shqmeruli_data = {
        "name": "Shqmeruli",
        "cuisine": "Georgian",
        "time_minutes": "80"
    }
    response = requests.put(f'{BASE_URL}/recipes/{real_id_khinkali}', json=shqmeruli_data, timeout=TIMEOUT_LIMIT)
    response.raise_for_status()

    print(f"განახლდა წარმატებით! სტატუსი: {response.status_code}")


    print(f"\n--- რეცეპტის წაშლა (DELETE) კონკრეტულ ID-ზე: {real_id_mtsvadi} ---")
    response = requests.delete(f'{BASE_URL}/recipes/{real_id_mtsvadi}', timeout=TIMEOUT_LIMIT)
    response.raise_for_status()

    print(f"წაიშალა წარმატებით! სტატუსი: {response.status_code}")

except HTTPError as e:
    print(f"HTTP შეცდომა: {e}")
except ConnectTimeout as e:
    print(f"კავშირის დრო ამოიწურა: {e}")
except Exception as e:
    print(f"მოულოდნელი შეცდომა: {e}")




