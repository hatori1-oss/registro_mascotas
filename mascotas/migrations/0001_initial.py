# Generated by Django 5.2 on 2025-04-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('raza', models.CharField(blank=True, max_length=100)),
                ('edad', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
