from flask import Blueprint, Flask, redirect, url_for
from controllers.generator_controller import GeneratorController

# Create a Blueprint for the API
api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Define routes under the Blueprint
api_blueprint.add_url_rule("/add", view_func=GeneratorController.addition, methods=["GET"])
api_blueprint.add_url_rule("/sub", view_func=GeneratorController.subtraction, methods=["GET"])
api_blueprint.add_url_rule("/mul", view_func=GeneratorController.multiplication, methods=["GET"])
api_blueprint.add_url_rule("/div", view_func=GeneratorController.division, methods=["GET"])
api_blueprint.add_url_rule("/random", view_func=GeneratorController.random_operation, methods=["GET"])
api_blueprint.add_url_rule('/', view_func=GeneratorController.root_redirect, methods=['GET'])

def register_routes(app: Flask):
    """
    Registers the API blueprint with the Flask app.

    :param app: Flask application instance
    """
    app.register_blueprint(api_blueprint)

    @app.route("/")
    def root():
        return GeneratorController.root_redirect()
