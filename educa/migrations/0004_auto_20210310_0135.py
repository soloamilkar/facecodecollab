# Generated by Django 3.1.7 on 2021-03-10 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0003_auto_20210307_1958'),
        ('educa', '0003_auto_20210310_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='framework',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='languages.framework'),
        ),
    ]
