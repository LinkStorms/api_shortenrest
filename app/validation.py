import validators

from settings import (
    TOKEN_LENGTH_RANGE,
    ALIAS_LENGTH_RANGE
)


def url_validation(url, url_name="Url", ignore_protocol=False):
    """ Raises an exception if url is not valid.
    """
    if not url:
        raise ValueError("Url is required.")

    if ignore_protocol:
        url_with_protocol = "http://" + url
        if not validators.url(url_with_protocol) and not validators.url(url):
            raise ValueError(f"{url_name} is not valid.")
    else:
        if not validators.url(url):
            raise ValueError(f"{url_name} is not valid.")


def token_validation(token, token_length_range=TOKEN_LENGTH_RANGE):
    """ Raises an exception if token is not valid.
    """
    min_length, max_length = token_length_range

    if not token:
        raise ValueError("Token is required.")

    if len(token) < min_length:
        raise ValueError(f"Token must be at least {min_length} characters long.")
    if len(token) > max_length:
        raise ValueError(f"Token must be less than {max_length} characters long.")


def alias_validation(token_name, alias_length_range=ALIAS_LENGTH_RANGE):
    """ Raises an exception if alias is not valid.
    """
    min_length, max_length = alias_length_range

    if not token_name:
        raise ValueError("Alias is required.")

    if len(token_name) < min_length:
        raise ValueError(f"Alias must be at least {min_length} characters long.")
    if len(token_name) > max_length:
        raise ValueError(f"Alias must be less than {max_length} characters long.")
