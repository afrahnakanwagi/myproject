# Generated by Django 5.0.6 on 2024-09-07 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalbook', '0010_alter_deffered_payments_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deffered_payments',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 18, 1, 15, 238058)),
        ),
        migrations.AlterField(
            model_name='deffered_payments',
            name='date_of_payment',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 18, 1, 15, 238058)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 18, 1, 15, 238058)),
        ),
    ]