# Generated by Django 4.2.4 on 2023-09-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geology', '0035_report_edit_date_alter_report_intro_repo'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='degree',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ("Diploma's degree", 'DA'), ("Bachelor's degree", 'BA'), ("Master's degree", 'MA'), ("Doctoral's degree", 'PHD'), ("Associate's degree", 'AA'), ('Teaching Assistant', 'Teaching Assistant'), ('Assistant Lecturer', 'Assistant Lecturer'), ('Assistant Professor', 'Assistant Professor')], null=True),
        ),
    ]