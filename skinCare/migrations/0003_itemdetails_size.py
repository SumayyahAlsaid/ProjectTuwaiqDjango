# Generated by Django 4.2.10 on 2024-03-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skinCare', '0002_remove_itemdetails_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdetails',
            name='size',
            field=models.IntegerField(null=True),
        ),
    ]
