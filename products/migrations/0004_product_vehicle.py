# Generated by Django 3.1.7 on 2021-03-08 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_fitment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vehicle',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
