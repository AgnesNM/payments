from django.db import models

# Create your models here.

class Payments (models.Model):
    phone_no = models.CharField(max_length=254),
    username = models.CharField(max_length=254),
    user_id_no = models.CharField(max_length=254)

    def __str__(self):
        return self.username