
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields
from flask_jwt_extended import create_access_token

blp = Blueprint(
    "auth",
    __name__,
    description="Authentication operations"
)


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


@blp.route("/login")
class Login(MethodView):

    @blp.arguments(LoginSchema)
    def post(self, data):

        # Demo credentials for this lab
        if (
            data["username"] != "test"
            or data["password"] != "test"
        ):
            abort(401, message="Invalid username or password")

        access_token = create_access_token(
            identity=data["username"]
        )

        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }, 200