# Generated by Django 4.1.6 on 2023-02-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=60, verbose_name='Nombres completos'),
        ),
    ]
