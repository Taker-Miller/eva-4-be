# Generated by Django 4.2.6 on 2023-11-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='saldo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(default='', max_length=100),
        ),
    ]