# Generated by Django 4.0.6 on 2022-07-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npm_crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastnews',
            name='date_published',
            field=models.CharField(max_length=100),
        ),
    ]