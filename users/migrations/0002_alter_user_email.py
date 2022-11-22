# Generated by Django 4.1.2 on 2022-11-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': '이미 존재하는 이메일입니다.'}, max_length=255, unique=True, verbose_name='email address'),
        ),
    ]