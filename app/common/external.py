import hashlib
import json

import requests

from app.config import config
from .error import ExternalAPIFailError


class Facebook():
    @classmethod
    def get_user(cls, user_id, access_token):
        result = requests.get(
                f'https://graph.facebook.com/{user_id}',
                params={
                    'fields': 'id,name,email',
                    'access_token': access_token,
                })
        if result.status_code != 200:
            raise ExternalAPIFailError('facebook', result)

        return result


class LastFM():
    @classmethod
    def _signiture(cls, method, token):
        sig_str = f'api_key{config.LASTFM_APP_ID}method{method}token{token}{config.LASTFM_APP_SECRET}'

        m = hashlib.md5()
        m.update(sig_str.encode())
        result = m.hexdigest()

        return result

    @classmethod
    def get_session(cls, token):
        method = 'auth.getSession'

        resp = requests.get(
                'https://ws.audioscrobbler.com/2.0',
                params={
                    'method': method,
                    'token': token,
                    'api_key': config.LASTFM_APP_ID,
                    'api_sig': cls._signiture(method, token),
                    'format': 'json',
                })
        result = json.loads(resp.text)

        name = result['lfm']['session'][0]['name'][0]
        session_key = result['lfm']['session'][0]['key'][0]

        return session_key, name
