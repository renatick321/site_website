# Generated by Django 3.0.2 on 2020-03-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200306_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, default='Neverland', max_length=30, null=True),
        ),
    ]