# Generated by Django 4.2 on 2023-04-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('groups', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='members_group', to='members.member'),
        ),
    ]