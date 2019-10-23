# Generated by Django 2.2.6 on 2019-10-23 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, verbose_name='휴대폰 번호')),
                ('email', models.CharField(max_length=30, verbose_name='이메일')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='partner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '파트너',
                'verbose_name_plural': '파트너',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, verbose_name='닉네임')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '클라이언트',
                'verbose_name_plural': '클라이언트',
                'ordering': ['id'],
            },
        ),
    ]
