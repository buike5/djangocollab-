from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class post(models.Model):
    Title = models.CharField(max_length=20)
    Body = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blog_post')
    Published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.Title
