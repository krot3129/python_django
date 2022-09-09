# Generated by Django 2.2 on 2022-09-09 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0010_auto_20220909_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='news_com',
        ),
        migrations.AddField(
            model_name='news',
            name='news_com',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.Comment'),
        ),
    ]
