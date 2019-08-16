# Generated by Django 2.2.4 on 2019-08-16 15:48

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resourceservice', '0002_resourcecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorySelectingOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourceservice.ResourceCategory')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_category', to='resourceservice.ResourcePage')),
            ],
            options={
                'verbose_name': 'ResourceCategory',
                'verbose_name_plural': 'ResourceCategories',
            },
        ),
    ]