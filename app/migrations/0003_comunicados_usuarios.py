# Generated by Django 3.0.2 on 2020-01-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comunicados'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicados',
            name='usuarios',
            field=models.ManyToManyField(to='app.Usuarios'),
        ),
    ]