# Generated by Django 4.2.4 on 2023-09-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geology', '0027_alter_author_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='cv',
            field=models.FileField(blank=True, default='mediafiles/cv/hind.txt', null=True, upload_to='cv'),
        ),
    ]