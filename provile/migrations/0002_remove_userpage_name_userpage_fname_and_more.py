# Generated by Django 4.2.4 on 2023-09-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpage',
            name='name',
        ),
        migrations.AddField(
            model_name='userpage',
            name='fname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userpage',
            name='gallery_img',
            field=models.ImageField(blank=True, null=True, upload_to='user_provile_img/'),
        ),
        migrations.AddField(
            model_name='userpage',
            name='lname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userpage',
            name='sname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userpage',
            name='tname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userpage',
            name='user_bio',
            field=models.CharField(max_length=200, null=True),
        ),
    ]