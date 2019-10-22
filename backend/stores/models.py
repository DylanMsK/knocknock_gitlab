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
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    review_cnt = models.IntegerField(default=0)
    view_cnt = models.IntegerField(default=0)
    options = models.ManyToManyField(Option)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.addr}'


class BusinessRegistration(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    business_registration_number = models.CharField(max_length=10)
    representative_name = models.CharField(max_length=30)
    business_address = models.CharField(max_length=100)
    registration_image = models.ImageField(upload_to='partners/certificates')
    business_commencement_date = models.DateField(null=True)
    business_type = models.CharField(max_length=30, null=True)
    business_item = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.company_name} | {self.partner.name}'