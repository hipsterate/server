from flask import Blueprint
from flask_restplus import Api, Resource, reqparse

from app.user.command import UserCommand


blueprint = Blueprint('user', __name__)
api = Api(blueprint)


@api.route('/signup')
class SignupAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        params = parser.parse_args()

        user_command = UserCommand()
        user_command.signup(**params)

        return {}


@api.route('/signin')
class SigninAPI(Resource):
    def post(self):
        user_command = UserCommand()
        user_command.signin()

        return {}
