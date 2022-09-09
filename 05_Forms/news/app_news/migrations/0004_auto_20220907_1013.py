# Generated by Django 2.2 on 2022-09-07 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_auto_20220907_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='comments',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_news.News'),
        ),
    ]
