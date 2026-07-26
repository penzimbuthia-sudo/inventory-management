import requests

BASE_URL = "http://127.0.0.1:5000"

def display_response(response):
    """
    Display API responses in a consistent format.
    """

    print("\nStatus:", response.status_code)
    print(response.json())

def view_inventory():

    response = requests.get(
        f"{BASE_URL}/inventory"
    )

    if response.status_code == 200:

        print("\nInventory")

        for item in response.json():

            print(
                f"""
    ID: {item['id']}
    Product: {item['product_name']}
    Brand: {item['brand']}
    Price: {item['price']}
    Stock: {item['stock']}
    -------------------------
    """
            )

    else:

        display_response(response)    

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

    display_response(response)

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

    display_response(response)

def delete_item():

    item_id = input(
        "Item ID: "
    )

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    display_response(response)

def search_product():

    barcode = input(
        "Barcode: "
    )

    response = requests.get(
        f"{BASE_URL}/product/{barcode}"
    )

    display_response(response)

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