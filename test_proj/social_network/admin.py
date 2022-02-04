from django.contrib import admin
from .models import (
    UserModel,
    Post
)

admin.site.register(UserModel)
admin.site.register(Post)


