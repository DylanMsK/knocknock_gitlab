from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import Partner

class Category(models.Model):
    main_category = models.CharField(max_length=30)
    sub_category = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.main_category} | {self.sub_category}'


class Option(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


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
    common_addr = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
    tags = models.TextField(blank=True, default='')
    price_avg = models.IntegerField(default=0)
    partner = models.ForeignKey(Partner, on_delete=models.SET_DEFAULT, default=0, blank=True)
    review_cnt = models.IntegerField(default=0)
    view_cnt = models.IntegerField(default=0)
    options = models.ManyToManyField(Option)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.addr}'