# Generated by Django 3.0.3 on 2020-03-17 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibreBadge', '0008_auto_20200317_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgetemplate',
            name='slug',
            field=models.CharField(max_length=50),
        ),
    ]
