# Generated by Django 5.1.1 on 2024-11-18 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_payment_trackingdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
