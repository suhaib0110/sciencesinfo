# Generated by Django 4.2.4 on 2023-08-23 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dectionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200, unique=True)),
                ('meaning', models.TextField()),
                ('pub_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
