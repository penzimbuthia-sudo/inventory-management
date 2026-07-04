import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():

    response = requests.get(
        f"{BASE_URL}/inventory"
    )

    print(response.json())

def add_item():

    product_name = input(
        "Product Name: "
    )

    brand = input(
        "Brand: "
    )

    price = float(
        input("Price: ")
    )

    stock = int(
        input("Stock: ")
    )

    response = requests.post(
        f"{BASE_URL}/inventory",
        json={
            "product_name": product_name,
            "brand": brand,
            "price": price,
            "stock": stock
        }
    )

    print(response.json())

def update_item():

    item_id = input(
        "Item ID: "
    )

    price = float(
        input("New Price: ")
    )

    stock = int(
        input("New Stock: ")
    )

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json={
            "price": price,
            "stock": stock
        }
    )

    print(response.json())

def delete_item():

    item_id = input(
        "Item ID: "
    )

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    print(response.json())

def search_product():

    barcode = input(
        "Barcode: "
    )

    response = requests.get(
        f"{BASE_URL}/product/{barcode}"
    )

    print(response.json())

while True:

    print("\nInventory System")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Search Product")
    print("6. Exit")

    choice = input("> ")

    if choice == "1":
        view_inventory()

    elif choice == "2":
        add_item()

    elif choice == "3":
        update_item()

    elif choice == "4":
        delete_item()

    elif choice == "5":
        search_product()

    elif choice == "6":
        break

    else:
        print("Invalid choice")