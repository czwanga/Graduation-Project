# Generated by Django 2.0 on 2018-03-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20171201_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.CharField(blank=True, max_length=200, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
