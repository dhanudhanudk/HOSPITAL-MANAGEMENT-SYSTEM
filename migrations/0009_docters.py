# Generated by Django 4.2.7 on 2024-04-01 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0008_delete_adminsign'),
    ]

    operations = [
        migrations.CreateModel(
            name='docters',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('specialist', models.CharField(max_length=100, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
