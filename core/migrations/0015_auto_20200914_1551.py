# Generated by Django 3.0.8 on 2020-09-14 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200914_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='liked_videos',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Video')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='likers',
            field=models.ManyToManyField(through='core.Like', to='core.UserProfile'),
        ),
    ]
