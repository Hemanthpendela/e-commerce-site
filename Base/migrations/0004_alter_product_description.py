# Generated by Django 3.2 on 2021-04-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_auto_20210424_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
