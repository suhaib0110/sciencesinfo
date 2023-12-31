# Generated by Django 4.2.4 on 2023-10-07 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geology', '0050_faq_answer_faq_answer_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(choices=[('Native Elements', 'Native Elements'), ('Sulfides', 'Sulfides'), ('Sulfates', 'Sulfates'), ('Halides', 'Halides'), ('Oxides', 'Oxides'), ('Carbinates', 'Carbinates'), ('Phosphates', 'Phosphates'), ('Silicates', 'Silicates'), ('Organic Minerals', 'Organic Minerals'), ('Other', 'Other')], verbose_name='Classes')),
                ('subgroups_sio', models.CharField(blank=True, choices=[('Nesosilicates', 'Nesosilicates'), ('Sorosilicates', 'Sorosilicates'), ('Cyclosilicates', 'Cyclosilicates'), ('Inosilicates', 'Inosilicates'), ('Phyllosilicates', 'Phyllosilicates'), ('Tectosilicates', 'Tectosilicates')], null=True, verbose_name='Silicates subgroup')),
                ('other_classes', models.CharField(blank=True, max_length=100, null=True, verbose_name='Other classes')),
                ('name', models.CharField(help_text='rock name..', max_length=200, unique=True)),
                ('intro', models.TextField(max_length=500)),
                ('mineral_img', models.ImageField(upload_to='Minerals/', verbose_name='Picture')),
                ('details', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Details')),
                ('key_words', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geology.author')),
                ('edit_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'pub_date',
            },
        ),
    ]
