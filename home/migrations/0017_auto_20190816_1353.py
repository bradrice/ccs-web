# Generated by Django 2.2.4 on 2019-08-16 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190816_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcecatsorderable',
            name='resource',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.DeleteModel(
            name='ResourceCatsOrderable',
        ),
    ]
