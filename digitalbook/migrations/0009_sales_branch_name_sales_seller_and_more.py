# Generated by Django 5.0.6 on 2024-09-07 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalbook', '0008_remove_sales_branch_remove_sales_sells_agent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='branch_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='seller',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='deffered_payments',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 12, 3, 47, 488894)),
        ),
        migrations.AlterField(
            model_name='deffered_payments',
            name='date_of_payment',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 12, 3, 47, 488894)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 7, 12, 3, 47, 486401)),
        ),
    ]