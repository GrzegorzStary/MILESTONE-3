# Generated by Django 5.2.1 on 2025-05-21 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_roomtype_remove_reservation_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservation.roomtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='name',
            field=models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite'), ('deluxe', 'Deluxe'), ('family', 'Family')], max_length=50, unique=True),
        ),
    ]
