# Generated by Django 2.0.5 on 2018-05-29 07:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item_list_app', '0003_auto_20180525_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='foundTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
