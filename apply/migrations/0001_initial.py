# Generated by Django 3.2.5 on 2021-07-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('student_id', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=15)),
                ('q1', models.TextField(max_length=300)),
                ('q2', models.TextField(max_length=300)),
                ('q3', models.TextField(max_length=300)),
                ('q4', models.TextField(max_length=300)),
                ('date', models.DateField()),
            ],
        ),
    ]
