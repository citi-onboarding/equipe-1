# Generated by Django 2.0 on 2017-12-06 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171206_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='É da equipe?'),
        ),
        migrations.AlterField(
            model_name='casa',
            name='foto',
            field=models.FileField(upload_to='oi/'),
        ),
    ]
