# Generated by Django 4.2 on 2023-05-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0021_remove_user_dislikes_remove_user_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]