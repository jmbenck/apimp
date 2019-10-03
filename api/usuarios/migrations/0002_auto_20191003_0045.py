# Generated by Django 2.2.6 on 2019-10-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='pontuacao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.IntegerField(choices=[('1', 'Masculino'), ('2', 'Feminino')], unique=True),
        ),
    ]
