# Generated by Django 4.2.4 on 2023-09-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geology', '0021_alter_author_user_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Certificates',
                'verbose_name_plural': 'Certificates',
            },
        ),
        migrations.CreateModel(
            name='ContactProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact Profile',
                'verbose_name_plural': 'Contact Profiles',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('score', models.IntegerField(blank=True, default=80, null=True)),
                ('is_key_skill', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.RemoveField(
            model_name='author',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='author',
            name='gallery_img',
        ),
        migrations.RemoveField(
            model_name='author',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='author',
            name='sname',
        ),
        migrations.RemoveField(
            model_name='author',
            name='tname',
        ),
        migrations.AddField(
            model_name='author',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AddField(
            model_name='author',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv'),
        ),
        migrations.AddField(
            model_name='author',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='user_bio',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='skills',
            field=models.ManyToManyField(blank=True, to='geology.skill'),
        ),
    ]