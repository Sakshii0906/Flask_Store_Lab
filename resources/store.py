
from flask.views import MethodView
from flask_smorest import Blueprint, abort

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

    def get(self):
        return {"stores": stores}


@blp.route("/store/<string:store_id>")
class Store(MethodView):

    def get(self, store_id):
        for store in stores:
            if store["id"] == store_id:
                return store

        abort(404, message="Store not found")

    def delete(self, store_id):
        for store in stores:
            if store["id"] == store_id:
                stores.remove(store)
                return {"message": "Store deleted successfully"}

        abort(404, message="Store not found")