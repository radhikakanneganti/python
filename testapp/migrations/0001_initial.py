# Generated by Django 3.2.9 on 2021-12-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('acctNumber', models.IntegerField()),
                ('dateofactopen', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acctNumber', models.IntegerField()),
                ('amount', models.FloatField()),
                ('dateofpurchase', models.DateTimeField()),
            ],
        ),
    ]
