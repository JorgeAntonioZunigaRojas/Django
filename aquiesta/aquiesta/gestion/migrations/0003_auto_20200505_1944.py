# Generated by Django 3.0.5 on 2020-05-06 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20200505_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(default='static/imagen_no_disponible.png', upload_to='empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(default='static/imagen_no_disponible.png', upload_to='empresa'),
        ),
    ]