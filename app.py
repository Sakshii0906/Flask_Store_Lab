from flask import Flask, request, jsonify

app = Flask(__name__)

stores = [
    {
        "id": 1,
        "name": "ABC Store",
        "location": "Vadodara"
    },
    {
        "id": 2,
        "name": "XYZ Store",
        "location": "Ahmedabad"
    }
]

products = [
    {
        "id": 1,
        "store_id": 1,
        "name": "Laptop",
        "price": 50000
    },
    {
        "id": 2,
        "store_id": 2,
        "name": "Mobile",
        "price": 20000
    }
]

@app.route("/")
def home():
    return "Flask Store API is running!"


@app.route("/stores", methods=["GET"])
def get_stores():
    return jsonify(stores)


@app.route("/stores", methods=["POST"])
def create_store():
    data = request.get_json()

    new_store = {
        "id": len(stores) + 1,
        "name": data["name"],
        "location": data["location"]
    }

    stores.append(new_store)

    return jsonify(new_store), 201


@app.route("/stores/<int:store_id>", methods=["GET"])
def get_store(store_id):
    for store in stores:
        if store["id"] == store_id:
            return jsonify(store)

    return jsonify({"message": "Store not found"}), 404

# 4. Create a product
@app.route("/stores/<int:store_id>/products", methods=["POST"])
def create_product(store_id):
    data = request.get_json()

    # Check whether store exists
    for store in stores:
        if store["id"] == store_id:

            new_product = {
                "id": len(products) + 1,
                "store_id": store_id,
                "name": data["name"],
                "price": data["price"]
            }

            products.append(new_product)

            return jsonify(new_product), 201

    return jsonify({"message": "Store not found"}), 404

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)