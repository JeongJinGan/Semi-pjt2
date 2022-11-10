from django.db import models
from django.conf import settings



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    day = models.DateTimeField()
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_post")
    park_address = models.CharField(max_length=80)
    pet = models.BooleanField(default = False)
    content = models.TextField()
    TIME_CHOICES = (
        ("00:00", "00:00"),
        ("01:00", "01:00"),
        ("02:00", "02:00"),
        ("03:00", "03:00"),
        ("04:00", "04:00"),
        ("05:00", "05:00"),
        ("06:00", "06:00"),
        ("07:00", "07:00"),
        ("08:00", "08:00"),
        ("09:00", "09:00"),
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
        ("18:00", "18:00"),
        ("19:00", "19:00"),
        ("20:00", "20:00"),
        ("21:00", "21:00"),
        ("22:00", "22:00"),
        ("23:00", "23:00"),
        ("24:00", "24:00"),
    )
    time = models.CharField(max_length=20,choices=TIME_CHOICES)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)