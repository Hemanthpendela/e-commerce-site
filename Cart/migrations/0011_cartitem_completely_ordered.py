# Generated by Django 3.2 on 2021-05-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='completely_ordered',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]