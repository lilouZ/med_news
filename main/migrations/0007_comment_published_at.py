# Generated by Django 3.0.8 on 2020-08-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
