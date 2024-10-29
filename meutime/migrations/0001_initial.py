# Generated by Django 5.1 on 2024-10-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('local_nasc', models.TextField(max_length=250)),
                ('posicao', models.CharField(max_length=15)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]