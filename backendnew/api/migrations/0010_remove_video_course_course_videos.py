# Generated by Django 5.2.1 on 2025-05-11 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_course_video_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='videos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.video'),
            preserve_default=False,
        ),
    ]
