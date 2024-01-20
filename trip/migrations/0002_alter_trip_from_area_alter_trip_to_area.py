# Generated by Django 4.1.1 on 2024-01-19 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='from_area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trips_from', to='trip.area'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='to_area',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='trips_to', to='trip.area'),
        ),
    ]
