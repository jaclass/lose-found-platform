# Generated by Django 2.0.5 on 2018-05-29 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_list_app', '0005_otheritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='foundTime',
            field=models.DateField(default=datetime.date(2018, 5, 29)),
        ),
        migrations.AlterField(
            model_name='otheritem',
            name='foundTime',
            field=models.DateField(default=datetime.date(2018, 5, 29)),
        ),
    ]