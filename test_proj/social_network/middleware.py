from django.utils import timezone
from rest_framework import status

from .models import UserModel


class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        assert hasattr(
            request, "user"
        ), "The UpdateLastActivityMiddleware requires authentication middleware to be installed."

        if request.user.is_authenticated:
            UserModel.objects.filter(id=request.user.id).update(
                last_activity=timezone.now()
            )

        return response


class UpdateLastLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        assert hasattr(
            request, "user"
        ), "The UpdateLastActivityMiddleware requires authentication middleware to be installed."

        if (
            request.method == "POST"
            and request.path == "/token/"
            and response.status_code == status.HTTP_200_OK
        ):
            UserModel.objects.filter(username=request._post['username']).update(
                last_login=timezone.now()
            )

        return response
