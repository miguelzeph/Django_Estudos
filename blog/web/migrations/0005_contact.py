# Generated by Django 3.1.5 on 2021-01-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_post_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
