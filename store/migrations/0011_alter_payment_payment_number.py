# Generated by Django 5.1.1 on 2024-11-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_payment_payment_menthod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
