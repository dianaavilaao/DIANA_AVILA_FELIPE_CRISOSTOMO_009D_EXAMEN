# Generated by Django 5.0.6 on 2024-06-27 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio_con_descuento', models.IntegerField()),
                ('precio_normal', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='productos/')),
            ],
        ),
    ]
