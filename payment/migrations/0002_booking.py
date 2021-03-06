# Generated by Django 3.0.4 on 2020-03-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_cusid', models.CharField(max_length=50)),
                ('stripe_chid', models.CharField(max_length=50)),
                ('boatid', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('seats', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('fromm', models.CharField(max_length=30)),
                ('to', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
