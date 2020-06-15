# Generated by Django 3.0.4 on 2020-06-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_booking_paymentmode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('ticket_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]