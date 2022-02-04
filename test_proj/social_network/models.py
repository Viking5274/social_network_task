from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserModel(User):
    last_activity = models.DateTimeField(default=now(), blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserModel, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=120, blank=False)
    text = models.TextField(max_length=1500, blank=False)
    created_at = models.DateTimeField(default=now(), blank=True)
    author = models.ForeignKey(to=UserModel, related_name='user_post', on_delete=models.CASCADE)
    likes = models.IntegerField

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return "{} {} {}".format(self.title, self.author.first_name, self.author.last_name)
