from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=25)
    melicode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="images/profiles", blank=True, null=True)
    phone = models.CharField(max_length=11)
    text = models.TextField()
    instagram = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=11)
    telegram = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
