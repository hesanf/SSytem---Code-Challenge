# Generated by Django 4.0.6 on 2022-07-05 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npm_crawler', '0002_alter_lastnews_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastnews',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
