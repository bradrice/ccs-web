# Generated by Django 2.2.4 on 2019-08-15 17:18

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190815_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='category',
        ),
        migrations.CreateModel(
            name='ResourceCatsOrderable',
            fields=[
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Resource')),
                ('resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='home.Resource')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]