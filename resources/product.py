from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    id = fields.Str(dump_only=True)

    store_id = fields.Str(
        required=True
    )

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    price = fields.Float(
        required=True,
        validate=validate.Range(min=0)
    )


class ProductUpdateSchema(Schema):
    name = fields.Str(
        validate=validate.Length(min=2, max=100)
    )

    price = fields.Float(
        validate=validate.Range(min=0)
    )


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

    @blp.response(200, ProductSchema(many=True))
    def get(self):
        return products

    @blp.arguments(ProductSchema)
    @blp.response(201, ProductSchema)
    def post(self, data):

        new_id = str(len(products) + 1)

        new_product = {
            "id": new_id,
            "store_id": data["store_id"],
            "name": data["name"],
            "price": data["price"]
        }

        products.append(new_product)

        return new_product


@blp.route("/product/<string:product_id>")
class Product(MethodView):

    @blp.response(200, ProductSchema)
    def get(self, product_id):

        for product in products:
            if product["id"] == product_id:
                return product

        abort(404, message="Product not found")


    @blp.arguments(ProductUpdateSchema)
    @blp.response(200, ProductSchema)
    def put(self, data, product_id):

        for product in products:

            if product["id"] == product_id:

                product["name"] = data.get(
                    "name",
                    product["name"]
                )

                product["price"] = data.get(
                    "price",
                    product["price"]
                )

                return product

        abort(404, message="Product not found")


    def delete(self, product_id):

        for product in products:

            if product["id"] == product_id:

                products.remove(product)

                return {
                    "message": "Product deleted successfully"
                }

        abort(404, message="Product not found")