# Generated by Django 2.2.4 on 2019-08-15 13:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190815_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
