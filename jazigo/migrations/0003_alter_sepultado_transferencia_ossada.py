# Generated by Django 4.2 on 2023-06-01 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jazigo', '0002_rename_jazigo_cemiterio_destino_transferenciadeossada_cemiterio_destino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepultado',
            name='transferencia_ossada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jazigo.transferenciadeossada'),
        ),
    ]
