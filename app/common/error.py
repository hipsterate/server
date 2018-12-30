class Error(Exception):
    pass


class ExternalAPIFailError(Error):
    message = 'fail to get response external API'

    def __init__(self, provider, response, *args, **kwargs):
        message = f'{self.message}: {provider}, {response.text}'
        super().__init__(self, message, *args, **kwargs)
