# Generated by Django 3.0.6 on 2020-05-12 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20200512_0706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bio',
            old_name='bio',
            new_name='summary',
        ),
    ]
