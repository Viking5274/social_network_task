from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from vote.models import VoteModel


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


class Post(VoteModel, models.Model):
    title = models.CharField(max_length=120, blank=False)
    text = models.TextField(max_length=1500, blank=False)
    created_at = models.DateTimeField(default=now(), blank=True)
    user = models.ForeignKey(to=UserModel, related_name='user_post', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return "{} {} {}".format(self.title, self.user.first_name, self.user.last_name)


class LikeDislikePost(models.Model):
    TYPES_CHOICES = (
        ("0", "None"),
        ("1", "Like"),
        ("-1", "Dislike"),
    )
    like_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    like_author=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    values = models.IntegerField(
        choices=TYPES_CHOICES,
        # default="None",
    )
    created = models.DateTimeField(auto_now_add=True)
