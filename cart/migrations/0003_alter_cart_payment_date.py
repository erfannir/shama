# Generated by Django 5.0.3 on 2024-08-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_delete_cartdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
