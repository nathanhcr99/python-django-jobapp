# Generated by Django 5.0 on 2024-01-09 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
    ]
