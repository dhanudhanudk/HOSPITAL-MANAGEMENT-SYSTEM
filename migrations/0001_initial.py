# Generated by Django 4.2.7 on 2024-02-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(max_length=100, null=True)),
                ('phonenumber', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=40, null=True)),
                ('date', models.IntegerField(max_length=500)),
            ],
        ),
    ]