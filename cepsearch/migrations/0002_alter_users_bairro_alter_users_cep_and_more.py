# Generated by Django 5.0.4 on 2024-04-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cepsearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='bairro',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='cep',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='users',
            name='cidade',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='rua',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='surname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='uf',
            field=models.CharField(max_length=255),
        ),
    ]
