from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    nickname = models.CharField(max_length=20)
    
    def __str__(self):
        return f'★[사용자] {self.id} | {self.nickname}'


class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='partner')
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)


    def __str__(self):
        return f'☆[파트너] {self.id}'
