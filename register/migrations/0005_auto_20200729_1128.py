# Generated by Django 3.0.8 on 2020-07-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20200729_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='register.Skill'),
        ),
    ]
