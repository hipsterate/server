from flask_restplus import inputs

from app.common.reqparse import base_parser, Inputs

from .enum import SocialProvider


def signup_parser():
    parser = base_parser.copy()
    parser.add_argument(
            'name', type=str, help='nickname (required for not social)')
    parser.add_argument(
            'email', type=inputs.email(check=True),
            help='email (required for not social)')
    parser.add_argument(
            'password', type=str, help='password (required for not social)')
    parser.add_argument(
            'social_provider', type=Inputs.enum(SocialProvider),
            choices=list(SocialProvider),
            help='social provider name (required for social)')
    parser.add_argument(
            'social_id', type=str,
            help='id of social account (required for social)')
    parser.add_argument(
            'social_access_token', type=str,
            help='access token of social account (required for social)')

    return parser


def connect_lastfm_parser():
    parser = base_parser.copy()
    parser.add_argument(
            'access_token', type=str, required=True,
            help='access token of lastfm')

    return parser
