# Generated by Django 3.0.5 on 2020-04-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_pedido_id_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='st_sgestion',
            field=models.CharField(default='EMITIDA', max_length=200),
        ),
    ]