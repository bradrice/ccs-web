# Generated by Django 2.2.4 on 2019-08-16 13:08

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190815_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='category',
            field=modelcluster.fields.ParentalManyToManyField(related_name='categories', to='home.ResourceCategory'),
        ),
        migrations.DeleteModel(
            name='ResourceCatsOrderable',
        ),
    ]