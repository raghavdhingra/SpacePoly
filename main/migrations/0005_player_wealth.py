# Generated by Django 2.2.2 on 2019-10-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191019_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='wealth',
            field=models.CharField(blank=True, default='30000', max_length=200, null=True),
        ),
    ]
