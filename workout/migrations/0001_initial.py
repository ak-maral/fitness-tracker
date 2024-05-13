# Generated by Django 5.0.4 on 2024-05-10 10:03

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate')], default='beginner', max_length=20)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('duration', models.FloatField(default=0)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 5, 10, 10, 3, 24, 387235, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
