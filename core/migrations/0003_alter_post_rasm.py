# Generated by Django 4.1 on 2022-12-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_rasm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rasm',
            field=models.ImageField(upload_to='rasmlar/'),
        ),
    ]
