from django.utils import timezone
from rest_framework import status

from .models import UserModel


class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # print(request.__dict__)
        # print(response.__dict__)
        # print(request.user.id)
        assert hasattr(
            request, "user"
        ), "The UpdateLastActivityMiddleware requires authentication middleware to be installed."
        if request.user.is_authenticated:
            UserModel.objects.filter(id=request.user.id).update(
                last_activity=timezone.now()
            )

        # print(request.__dict__)
        # print(response.__dict__)
        if (
            request.method == "POST"
            and request.path == "/token/"
            and response == status.HTTP_200_OK
        ):
            print("true")
        return response
