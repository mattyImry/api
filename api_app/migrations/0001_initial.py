# Generated by Django 3.2.8 on 2021-10-18 15:08

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('location_name', models.CharField(blank=True, max_length=80, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address', models.CharField(max_length=80)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
