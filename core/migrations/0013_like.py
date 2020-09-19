# Generated by Django 3.0.8 on 2020-09-14 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_userprofile_liked_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
                ('liked_videos', models.ManyToManyField(null=True, to='core.Video')),
            ],
        ),
    ]
