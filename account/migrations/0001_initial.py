# Generated by Django 3.1.7 on 2021-03-04 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('is_active', models.BooleanField(default=True)),
                ('is_tutor', models.BooleanField(default=False)),
                ('languages', models.ManyToManyField(blank=True, related_name='accounts', to='languages.Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
