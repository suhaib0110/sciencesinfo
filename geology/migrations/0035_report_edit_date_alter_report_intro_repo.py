# Generated by Django 4.2.4 on 2023-09-15 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('geology', '0034_alter_report_edit_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='report',
            name='intro_repo',
            field=models.TextField(blank=True, null=True),
        ),
    ]