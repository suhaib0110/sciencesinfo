# Generated by Django 4.2.4 on 2023-08-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geology', '0005_remove_report_repo_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_img', models.ImageField(upload_to='repo_img/')),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='repo_img',
        ),
    ]
