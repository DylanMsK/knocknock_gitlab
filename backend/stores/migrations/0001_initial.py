# Generated by Django 2.2.6 on 2019-10-22 08:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.CharField(max_length=30)),
                ('sub_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, default='')),
                ('lon', models.FloatField(validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('lat', models.FloatField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('thumbnail', models.TextField(blank=True, default='')),
                ('contact', models.CharField(blank=True, default='', max_length=15)),
                ('road_addr', models.CharField(max_length=50)),
                ('common_addr', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=50)),
                ('tags', models.TextField(blank=True, default='')),
                ('price_avg', models.IntegerField(default=0)),
                ('review_cnt', models.IntegerField(default=0)),
                ('view_cnt', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stores.Category')),
                ('options', models.ManyToManyField(to='stores.Option')),
                ('partner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('business_registration_number', models.CharField(max_length=10)),
                ('representative_name', models.CharField(max_length=30)),
                ('business_address', models.CharField(max_length=100)),
                ('registration_image', models.ImageField(upload_to='partners/certificates')),
                ('business_commencement_date', models.DateField(null=True)),
                ('business_type', models.CharField(max_length=30, null=True)),
                ('business_item', models.CharField(max_length=30, null=True)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Partner')),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stores.Store')),
            ],
        ),
    ]
