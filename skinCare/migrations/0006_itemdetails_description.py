# Generated by Django 4.2.10 on 2024-03-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skinCare', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdetails',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
