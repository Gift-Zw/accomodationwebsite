# Generated by Django 3.0.7 on 2022-03-21 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
