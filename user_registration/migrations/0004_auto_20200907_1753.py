# Generated by Django 2.2.16 on 2020-09-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0003_remove_verification_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
