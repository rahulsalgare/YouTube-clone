# Generated by Django 3.0.8 on 2020-09-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200914_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='liker',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='liked_videos',
            field=models.ManyToManyField(null=True, to='core.Video'),
        ),
    ]