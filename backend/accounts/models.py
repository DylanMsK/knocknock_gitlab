from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    
    def __str__(self):
        return "★[사용자] {} | {}".format(self.id, self.nickname)


class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "☆[파트너] {} | {}".format(self.id)
        