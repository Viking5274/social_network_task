from django.contrib import admin
from .models import (
    UserModel,
    Post,
    Like
)

admin.site.register(UserModel)
admin.site.register(Post)
admin.site.register(Like)



