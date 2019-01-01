from flask import Blueprint
from flask_restplus import Api, Resource, reqparse
from flask_login import login_user, current_user, login_required

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
            user_command.signup(params.name, params.email, params.password)
        else:
            user_command.social_signup(
                    params.social_provider, params.social_id,
                    params.social_access_token)

        return {}


@api.route('/signin')
class Signin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('social_provider', type=str)
        parser.add_argument('social_id', type=str)
        parser.add_argument('social_access_token', type=str)
        params = parser.parse_args()

        user_query = UserQuery()

        if params.social_provider is None:
            user = user_query.validate_password(
                    params.name, params.email, params.password)
        else:
            user = user_query.validate_social_access_token(
                    params.social_provider, params.social_id,
                    params.social_access_token)

        login_user(user)

        return {}


@api.route('/connectlastfm')
class ConnectLastFM(Resource):
    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, required=True)
        params = parser.parse_args()

        user_command = UserCommand()
        user_command.connect_lastfm(current_user.id, params.token)

        return {}
