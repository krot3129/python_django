# Generated by Django 2.2 on 2022-08-31 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0002_auto_20220831_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements_app.Type'),
        ),
    ]
