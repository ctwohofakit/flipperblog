from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


class Status(models.Model):
    name=models.CharField(max_length=128)
    description=models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE #delete key if reocrd is deleted
    )
    status=models.ForeignKey(
        Status,
        on_delete=models.CASCADE #tell us waht django should when this fkey is deleted
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])

    def __str__(self):
        return self.title
