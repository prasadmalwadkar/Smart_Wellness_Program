# Generated by Django 3.1.1 on 2021-05-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_patientdischargedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='admit',
            field=models.BooleanField(default=False),
        ),
    ]