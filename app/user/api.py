from flask import Blueprint
from flask_restplus import Api, Resource
from flask_login import login_user, current_user, login_required

from .reqparse import signup_parser, connect_lastfm_parser
from .command import UserCommand
from .query import UserQuery


blueprint = Blueprint('user', __name__)
api = Api(blueprint)


@api.route('/signup')
class Signup(Resource):
    @api.expect(signup_parser())
    def post(self):
        params = signup_parser().parse_args()

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
    @api.expect(signup_parser())
    def post(self):
        params = signup_parser().parse_args()

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
    @api.expect(connect_lastfm_parser())
    @login_required
    def post(self):
        params = connect_lastfm_parser.parse_args()

        user_command = UserCommand()
        user_command.connect_lastfm(current_user.id, params.token)

        return {}
