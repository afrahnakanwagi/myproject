# Generated by Django 5.0.6 on 2024-08-13 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalbook', '0002_stockx_stock_id_stockx_stock_branch_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockx',
            old_name='stock_price',
            new_name='issued_quantity',
        ),
        migrations.RenameField(
            model_name='stockx',
            old_name='stock_name',
            new_name='item_name',
        ),
        migrations.RenameField(
            model_name='stockx',
            old_name='stock_tonnage',
            new_name='total_quantity',
        ),
        migrations.RenameField(
            model_name='stockx',
            old_name='stock_cost',
            new_name='unit_cost',
        ),
        migrations.AddField(
            model_name='stockx',
            name='unit_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('amount_received', models.IntegerField(blank=True, default=0, null=True)),
                ('issued_to', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitalbook.stockx')),
            ],
        ),
    ]