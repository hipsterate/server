from flask_restplus import reqparse


def signup_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('social_provider', type=str)
    parser.add_argument('social_id', type=str)
    parser.add_argument('social_access_token', type=str)

    return parser


def connect_lastfm_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('token', type=str, required=True)

    return parser
