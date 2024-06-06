# Generated by Django 4.2.11 on 2024-06-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=100, unique=True)),
                ('senha', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
