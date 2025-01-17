# Generated by Django 3.0.3 on 2020-11-02 09:10

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(blank=True, max_length=200, null=True)),
                ('emp_email', models.CharField(blank=True, max_length=200, null=True)),
                ('emp_ID', models.IntegerField()),
                ('date_of_employement', models.DateField()),
                ('designation', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('salary', models.IntegerField()),
                ('health_cert_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=200, null=True)),
                ('amount_requisitioned', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField()),
                ('requisitioned_by', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('sold_at', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Supllies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=200, null=True)),
                ('supplier', models.CharField(blank=True, max_length=200, null=True)),
                ('quanitity', models.IntegerField()),
                ('date', models.DateField()),
                ('balance', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('checkedin', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
