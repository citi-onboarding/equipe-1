# Generated by Django 2.0 on 2017-12-14 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20171214_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='foto',
            field=models.FileField(upload_to='static/images/casas/'),
        ),
    ]
