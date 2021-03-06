from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserModel(AbstractUser):
    last_activity = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return "{} {}".format(self.username, self.last_name)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserModel, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=120, blank=False)
    text = models.TextField(max_length=1500, blank=False)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    user = models.ForeignKey(
        to=UserModel, related_name="user_post", on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(UserModel, through="Like", blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return "{} {} {}".format(self.title, self.user.first_name, self.user.last_name)


class Like(models.Model):
    status = models.BooleanField(default=None)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        try:
            obj = Like.objects.get(user=self.user, post=self.post)
            obj.status = self.status
            super(Like, obj).save(*args, **kwargs)
        except:
            super(Like, self).save(*args, **kwargs)
