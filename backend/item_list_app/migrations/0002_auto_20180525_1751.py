# Generated by Django 2.0.5 on 2018-05-25 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='foundTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
