# Generated by Django 4.1 on 2022-09-28 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_rename_sensor_id_measurements_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]