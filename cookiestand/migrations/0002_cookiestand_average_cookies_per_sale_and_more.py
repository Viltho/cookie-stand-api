# Generated by Django 4.1.5 on 2023-07-13 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookiestand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookiestand',
            name='average_cookies_per_sale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='hourly_sales',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='maximum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='minimum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
    ]