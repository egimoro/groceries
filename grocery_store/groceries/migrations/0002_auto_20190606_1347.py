# Generated by Django 2.2.1 on 2019-06-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceries',
            name='price',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='groceries',
            name='quantity',
            field=models.IntegerField(default=None),
        ),
    ]
