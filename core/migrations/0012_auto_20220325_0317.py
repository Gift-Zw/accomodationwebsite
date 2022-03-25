# Generated by Django 3.0.7 on 2022-03-25 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landlords', '0002_landlordprofile_user'),
        ('core', '0011_booking_landlord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlords.LandlordProfile'),
        ),
    ]
