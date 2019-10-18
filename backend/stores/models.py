from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import Partner

# Create your models here.
class Category(models.Model):
    main_category = models.CharField(max_length=30)
    sub_category = models.CharField(max_length=30)


class Store(models.Model):
    origin_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=True, default='')
    lon = models.FloatField(validators=[MaxValueValidator(180), MinValueValidator(-180)])
    lat = models.FloatField(validators=[MaxValueValidator(90), MinValueValidator(-90)])
    thumbnail = models.TextField(blank=True, default='')
    contact = models.CharField(max_length=15, blank=True, default='')
    road_addr = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
    tags = models.TextField(blank=True, default='')
    price_average = models.IntegerField(default=0)
    parking = models.BooleanField(default=False)
    booking = models.BooleanField(default=False)
    group_seat = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    togo = models.BooleanField(default=False)
    partner = models.ForeignKey(Partner, on_delete=models.SET_DEFAULT, default=0)
    review_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    