# Generated by Django 5.1.2 on 2025-04-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='max_spend',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
