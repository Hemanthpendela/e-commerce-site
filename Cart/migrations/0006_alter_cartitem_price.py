# Generated by Django 3.2 on 2021-04-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0005_auto_20210427_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]