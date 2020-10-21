from flask import Blueprint, request
from controllers import auth as controller
from utils.formatters import create_response

auth_blueprint = Blueprint('auth', __name__, url_prefix='/api')


@auth_blueprint.route('/auth/', methods=['POST'])
def make_auth():
    if request.method == 'POST':
        if not request.authorization:
            return create_response("Login is required", 401)

        response, status = controller.authentication(
            dict(request.authorization)
        )

        return create_response(response, status)
