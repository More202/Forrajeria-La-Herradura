# Generated by Django 5.0.6 on 2024-08-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARCAS', '0008_producto_obs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='marca',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(to='MARCAS.categoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='edad',
            field=models.ManyToManyField(to='MARCAS.edad'),
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.ManyToManyField(to='MARCAS.marca'),
        ),
    ]
