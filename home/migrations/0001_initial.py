# Generated by Django 5.1.1 on 2025-07-10 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
            ],
        ),
    ]
