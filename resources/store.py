
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
from flask_jwt_extended import jwt_required

blp = Blueprint(
    "stores",
    __name__,
    description="Operations on stores"
)

stores = [
    {
        "id": "1",
        "name": "ABC Store",
        "location": "Vadodara"
    },
    {
        "id": "2",
        "name": "XYZ Store",
        "location": "Ahmedabad"
    }
]


@blp.route("/store")
class StoreList(MethodView):

    @jwt_required()
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores

    @jwt_required()
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, data):
        new_id = str(len(stores) + 1)

        new_store = {
            "id": new_id,
            "name": data["name"],
            "location": data["location"]
        }

        stores.append(new_store)
        return new_store


@blp.route("/store/<string:store_id>")
class Store(MethodView):

    @jwt_required()
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        for store in stores:
            if store["id"] == store_id:
                return store

        abort(404, message="Store not found")

    @jwt_required()
    def delete(self, store_id):
        for store in stores:
            if store["id"] == store_id:
                stores.remove(store)
                return {"message": "Store deleted successfully"}

        abort(404, message="Store not found")