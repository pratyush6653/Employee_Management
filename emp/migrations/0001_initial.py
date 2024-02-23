# Generated by Django 5.0.2 on 2024-02-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emp_Id', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('working', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
