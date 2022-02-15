from django.contrib import admin
from .models import (
    UserModel,
    Post,
    # LikeDislikePost
)

admin.site.register(UserModel)
admin.site.register(Post)
# admin.site.register(LikeDislikePost)



