# Generated by Django 3.0.3 on 2020-03-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20200322_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='description',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
