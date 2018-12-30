import requests


class Facebook():
    @classmethod
    def get_user(cls, id_, access_token):
        result = requests.get(f'https://graph.facebook.com/{id_}?fields=id,name,email&access_token={access_token}')
        if result.status_code != 200:
            raise ValueError()

        return result
