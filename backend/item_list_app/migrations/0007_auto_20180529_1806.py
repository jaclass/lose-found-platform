# Generated by Django 2.0.5 on 2018-05-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_list_app', '0006_auto_20180529_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='foundTime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='otheritem',
            name='foundTime',
            field=models.DateField(),
        ),
    ]
