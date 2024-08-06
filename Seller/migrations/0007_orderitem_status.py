# Generated by Django 5.0.7 on 2024-08-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0006_alter_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('accepted', 'accepted'), ('packed', 'packed'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='accepted', max_length=10),
        ),
    ]
