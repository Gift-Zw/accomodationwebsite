# Generated by Django 3.0.7 on 2022-03-25 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20220325_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='landlord',
            field=models.CharField(max_length=100),
        ),
    ]
