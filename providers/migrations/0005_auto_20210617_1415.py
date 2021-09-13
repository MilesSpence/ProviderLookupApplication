# Generated by Django 3.2.4 on 2021-06-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0004_auto_20210616_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerfull',
            name='businessZipcode',
            field=models.CharField(blank=True, db_index=True, default='none', max_length=25),
        ),
        migrations.AlterField(
            model_name='providerfull',
            name='firstname',
            field=models.CharField(blank=True, db_index=True, default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='providerfull',
            name='lastname',
            field=models.CharField(blank=True, db_index=True, default='none', max_length=50),
        ),
    ]
