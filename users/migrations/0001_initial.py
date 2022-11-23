# Generated by Django 4.1.2 on 2022-11-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(error_messages={'unique': '이미 존재하는 이메일입니다.'}, max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('nickname', models.CharField(default='', error_messages={'unique': '이미 존재하는 닉네임입니다.'}, max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
