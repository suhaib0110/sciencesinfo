# Generated by Django 4.2.4 on 2023-10-26 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provile', '0028_contactprofile_is_sent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactprofile',
            options={'get_latest_by': 'timestamp'},
        ),
    ]
