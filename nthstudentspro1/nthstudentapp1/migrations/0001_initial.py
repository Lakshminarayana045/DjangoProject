# Generated by Django 4.1.7 on 2023-04-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mainpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('coursename', models.CharField(max_length=50)),
                ('emailid', models.EmailField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('hometown', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('percentage', models.IntegerField()),
                ('passedoutyear', models.IntegerField()),
            ],
        ),
    ]
