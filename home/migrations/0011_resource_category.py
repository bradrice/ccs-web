# Generated by Django 2.2.4 on 2019-08-15 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_resourcecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.ResourceCategory'),
        ),
    ]