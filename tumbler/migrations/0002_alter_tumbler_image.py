# Generated by Django 5.1.2 on 2024-12-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tumbler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tumbler',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
