# Generated by Django 3.1.7 on 2021-03-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210304_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='framework',
            new_name='frameworks',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='language',
            new_name='languages',
        ),
        migrations.AddField(
            model_name='account',
            name='github',
            field=models.URLField(blank=True, verbose_name='github'),
        ),
    ]
