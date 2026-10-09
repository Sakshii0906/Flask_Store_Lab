
from flask import Flask
from flask_smorest import Api

from resources.store import blp as StoreBlueprint
from resources.product import blp as ProductBlueprint
from datetime import timedelta
from flask_jwt_extended import JWTManager
from auth import blp as AuthBlueprint
import os


app = Flask(__name__)

# Flask-Smorest configuration
app.config["API_TITLE"] = "Flask Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = (
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
)

app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)

jwt = JWTManager(app)

# Initialize API
api = Api(app)

# Register Blueprints
api.register_blueprint(StoreBlueprint)
api.register_blueprint(ProductBlueprint)
api.register_blueprint(AuthBlueprint)


@app.route("/")
def home():
    return "Flask Store API is running!"


if __name__ == "__main__":
    app.run(debug=True)