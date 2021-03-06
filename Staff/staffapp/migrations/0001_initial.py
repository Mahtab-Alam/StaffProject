# Generated by Django 3.1.2 on 2021-03-25 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('emp_code', models.CharField(max_length=12)),
                ('company', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
