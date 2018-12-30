from app.common.error import Error


class ValidatePasswordError(Error):
    message = 'password validation failed'


class ValidateAccessTokenError(Error):
    message = 'social access token validation failed'


class NotSupportedProviderError(Error):
    message = 'not supported social provider'

    def __init__(self, provider, *args, **kwargs):
        message = f'{self.message}: {provider}'
        super().__init__(self, message, *args, **kwargs)
