# Generated by Django 3.0.6 on 2020-05-13 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20200512_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='links_to',
            field=models.CharField(default='#', max_length=50),
            preserve_default=False,
        ),
    ]