# Generated by Django 4.2.4 on 2023-09-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provile', '0018_alter_mediaurl_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='images',
            field=models.ImageField(blank=True, default='/certificate/work-img.jpg', null=True, upload_to='certificate/'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='images',
            field=models.ImageField(blank=True, default='/certificate/work-img.jpg', null=True, upload_to='certificate/'),
        ),
    ]
