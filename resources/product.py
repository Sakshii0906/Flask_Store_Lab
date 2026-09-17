from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields

class ProductUpdateSchema(Schema):
    name = fields.String()
    price = fields.Float()

blp = Blueprint(
    "products",
    __name__,
    description="Operations on products"
)

products = [
    {
        "id": "1",
        "store_id": "1",
        "name": "Laptop",
        "price": 50000
    },
    {
        "id": "2",
        "store_id": "2",
        "name": "Mobile",
        "price": 20000
    }
]


@blp.route("/product")
class ProductList(MethodView):

    def get(self):
        return {"products": products}


@blp.route("/product/<string:product_id>")
class Product(MethodView):

    def get(self, product_id):
        for product in products:
            if product["id"] == product_id:
                return product

        abort(404, message="Product not found")

    @blp.arguments(ProductUpdateSchema)
    def put(self, data, product_id):
        for product in products:
            if product["id"] == product_id:
                product["name"] = data.get(
                    "name", product["name"]
                )
                product["price"] = data.get(
                    "price", product["price"]
                )
                return product

        abort(404, message="Product not found")

        for product in products:
            if product["id"] == product_id:
                product["name"] = data.get("name", product["name"])
                product["price"] = data.get("price", product["price"])
                return product

        abort(404, message="Product not found")

    def delete(self, product_id):
        for product in products:
            if product["id"] == product_id:
                products.remove(product)
                return {"message": "Product deleted successfully"}

        abort(404, message="Product not found")