# Generated by Django 3.0.2 on 2020-01-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('available', 'Available'), ('sold', 'Sold'), ('delisted', 'Delisted')], max_length=9)),
                ('year', models.CharField(blank=True, max_length=6)),
                ('make', models.CharField(blank=True, max_length=30)),
                ('model', models.CharField(blank=True, max_length=30)),
                ('vin', models.CharField(blank=True, max_length=30)),
                ('color', models.CharField(blank=True, max_length=30)),
                ('mileage', models.CharField(blank=True, max_length=9)),
                ('price', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]
