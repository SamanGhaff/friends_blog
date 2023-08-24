from django.db import models


class Massage(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.title


class OurInformation(models.Model):
    address = models.CharField(max_length=100)
    link_address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
