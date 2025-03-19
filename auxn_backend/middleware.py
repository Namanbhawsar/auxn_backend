import threading

_user = threading.local()


class CurrentUserMiddleware:
    """Middleware to store the current user in thread-local storage."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _user.request_user = request.user if request.user.is_authenticated else None
        response = self.get_response(request)
        _user.request_user = None  # Cleanup after request
        return response
