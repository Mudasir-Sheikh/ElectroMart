# Generated by Django 5.1.1 on 2024-11-24 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_payment_payment_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='postal_code',
        ),
    ]
