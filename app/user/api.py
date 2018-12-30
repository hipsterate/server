from flask import Blueprint
from flask_restplus import Api, Resource, reqparse

from app.user.command import UserCommand
from app.user.query import UserQuery


blueprint = Blueprint('user', __name__)
api = Api(blueprint)


@api.route('/signup')
class Signup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('social_provider', type=str)
        parser.add_argument('social_id', type=str)
        parser.add_argument('social_access_token', type=str)
        params = parser.parse_args()

        user_command = UserCommand()
        if params.social_provider is None:
            user_command.signup(**params)
        else:
            user_command.social_signup(**params)

        return {}


@api.route('/signin')
class SigninAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('provider', type=str)
        parser.add_argument('access_token', type=str)
        params = parser.parse_args()

        user_query = UserQuery()
        user_command = UserCommand()

        if params.provider is None:
            if not user_query.validate_password(params.email, params.password):
                raise ValueError()

            user = user_query.get_user(email=params.email)
            user_command.signin(user)
        elif params.provider == 'facebook':
            if not user_query.validate_facebook_access_token(
                    params.access_token):
                raise ValueError()
        else:
            raise ValueError()

        return {}
