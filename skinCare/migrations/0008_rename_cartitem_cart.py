# Generated by Django 4.2.10 on 2024-03-11 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skinCare', '0007_rename_cart_cartitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItem',
            new_name='Cart',
        ),
    ]
