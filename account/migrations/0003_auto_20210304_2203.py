# Generated by Django 3.1.7 on 2021-03-04 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
        ('account', '0002_auto_20210304_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='framework',
            field=models.ManyToManyField(blank=True, related_name='account', to='languages.Framework'),
        ),
        migrations.AlterField(
            model_name='account',
            name='language',
            field=models.ManyToManyField(blank=True, related_name='account', to='languages.Language'),
        ),
    ]
