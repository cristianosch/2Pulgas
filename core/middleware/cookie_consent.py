from django.shortcuts import redirect

class CookieConsentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.COOKIES.get('cookie_consent'):
            response.set_cookie('cookie_consent', 'false')
        return response
    