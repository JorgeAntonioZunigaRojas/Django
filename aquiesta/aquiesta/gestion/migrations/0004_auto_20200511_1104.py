# Generated by Django 3.0.5 on 2020-05-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20200505_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='tipo_doc_iden',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
