# Generated by Django 3.0.8 on 2020-09-22 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200922_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subscribed_channels',
            field=models.ManyToManyField(null=True, to='core.Channel'),
        ),
    ]
