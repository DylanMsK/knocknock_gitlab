# Generated by Django 2.2.6 on 2019-10-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='addr',
            field=models.CharField(blank=True, max_length=150, verbose_name='지번 주소'),
        ),
        migrations.AlterField(
            model_name='store',
            name='common_addr',
            field=models.CharField(max_length=150, verbose_name='시구'),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=150, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='store',
            name='road_addr',
            field=models.CharField(blank=True, max_length=150, verbose_name='도로명 주소'),
        ),
    ]
