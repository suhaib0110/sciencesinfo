# Generated by Django 4.2.4 on 2023-09-23 08:16

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geology', '0042_alter_report_repo_prograph'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='repo_prograph_users',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='report',
            name='repo_prograph',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Text'),
        ),
    ]