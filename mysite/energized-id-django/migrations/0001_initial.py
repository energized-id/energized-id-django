# Generated by Django 3.0.2 on 2020-02-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_title', models.CharField(max_length=200)),
                ('welcome_content', models.TextField()),
                ('welcome_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
