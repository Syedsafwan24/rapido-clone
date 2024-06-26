# Generated by Django 5.0.2 on 2024-04-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_driverdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('user_type', models.CharField(choices=[('Captain', 'Captain'), ('Customer', 'Customer')], max_length=8)),
                ('query_type', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
    ]
