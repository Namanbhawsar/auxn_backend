from threading import local

_user = local()


def get_current_user():
    """Retrieve the current user from thread-local storage."""
    return getattr(_user, 'request_user', None)