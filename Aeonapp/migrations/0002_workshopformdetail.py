# Generated by Django 5.0.6 on 2024-06-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aeonapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopFormDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phoneno', models.IntegerField(max_length=10)),
                ('profession', models.CharField(max_length=25)),
                ('institute', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=25)),
                ('queries', models.CharField(max_length=100)),
            ],
        ),
    ]
