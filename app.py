import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 450,
        "stock": 20
    }
]

def find_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None

def fetch_product(barcode):

    url = (
        f"https://world.openfoodfacts.org/api/v0/product/"
        f"{barcode}.json"
    )

    headers = {
        "User-Agent": "InventoryManagementLab/1.0 (student@example.com)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:
        print("ERROR:", e)
        return None

@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API"
    })

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):

    item = find_item(item_id)

    if item:
        return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

@app.route("/inventory", methods=["POST"])
def create_item():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No JSON data provided"
        }), 400

    required_fields = [
        "product_name",
        "brand",
        "price",
        "stock"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "error": f"{field} is required"
            }), 400

    if inventory:
        new_id = max(item["id"] for item in inventory) + 1
    else:
        new_id = 1

    new_item = {
        "id": new_id,
        "product_name": data["product_name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    item = find_item(item_id)

    if not item:
        return jsonify({
            "error": "Item not found"
        }), 404

    data = request.get_json()

    item["price"] = data.get("price", item["price"])
    item["stock"] = data.get("stock", item["stock"])
    item["product_name"] = data.get(
        "product_name",
        item["product_name"]
    )
    item["brand"] = data.get(
        "brand",
        item["brand"]
    )

    return jsonify(item)

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    item = find_item(item_id)

    if not item:
        return jsonify({
            "error": "Item not found"
        }), 404

    inventory.remove(item)

    return jsonify({
        "message": "Item deleted successfully"
    }), 200

@app.route("/inventory/search/<brand>", methods=["GET"])
def search_brand(brand):

    results = [
        item
        for item in inventory
        if item["brand"].lower() == brand.lower()
    ]

    if not results:
        return jsonify({
            "error": "No products found"
        }), 404

    return jsonify(results), 200

@app.route("/product/<barcode>", methods=["GET"])
def get_product(barcode):

    data = fetch_product(barcode)

    if data is None:

        return jsonify({
            "error": "Unable to reach OpenFoodFacts"
        }), 503

    if data.get("status") != 1:

        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify(data)

@app.route("/import/<barcode>", methods=["POST"])
def import_product(barcode):

    data = fetch_product(barcode)

    if data is None:

        return jsonify({
            "error": "Unable to reach OpenFoodFacts"
        }), 503

    if data.get("status") != 1:

        return jsonify({
            "error": "Product not found"
        }), 404

    product = data["product"]

    if inventory:
        new_id = max(item["id"] for item in inventory) + 1
    else:
        new_id = 1

    new_item = {
        "id": new_id,
        "product_name": product.get(
            "product_name",
            "Unknown Product"
        ),
        "brand": product.get(
            "brands",
            "Unknown Brand"
        ),
        "barcode": barcode,
        "ingredients": product.get(
            "ingredients_text",
            "Not available"
        ),
        "price": 0,
        "stock": 0
    }

    inventory.append(new_item)

    return jsonify({
        "message": "Product imported successfully",
        "item": new_item
    }), 201

if __name__ == "__main__":
    app.run(debug=True)