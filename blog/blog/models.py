from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150, help_text="required, max_lenght=150")
    text = models.TextField(max_length=2000, help_text="required, max_lenght=2000")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f'"{self.title}" from {self.author}'
