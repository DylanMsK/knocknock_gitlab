# Generated by Django 2.2.6 on 2019-10-28 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.Client', verbose_name='클라이언트')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='stores.Store', verbose_name='가게')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerCommnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_comments', to='accounts.Partner', verbose_name='파트너')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_comments', to='stores.Review', verbose_name='답글')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_comments', to='stores.Store', verbose_name='가게')),
            ],
        ),
    ]
