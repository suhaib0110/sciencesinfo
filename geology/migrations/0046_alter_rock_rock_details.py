# Generated by Django 4.2.4 on 2023-09-24 09:04

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geology', '0045_alter_rock_rock_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rock',
            name='rock_details',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]