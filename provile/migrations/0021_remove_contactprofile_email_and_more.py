# Generated by Django 4.2.4 on 2023-09-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provile', '0020_alter_mediaurl_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contactprofile',
            name='name',
        ),
        migrations.AddField(
            model_name='contactprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contactprofile',
            name='replay',
            field=models.TextField(blank=True, null=True, verbose_name='Replay'),
        ),
        migrations.AddField(
            model_name='contactprofile',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Title'),
            preserve_default=False,
        ),
    ]