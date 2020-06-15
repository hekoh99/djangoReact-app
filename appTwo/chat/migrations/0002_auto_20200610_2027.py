# Generated by Django 3.0.7 on 2020-06-10 20:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chatting',
            new_name='Chat',
        ),
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ('-create_dt',), 'verbose_name': 'chat', 'verbose_name_plural': 'chats'},
        ),
    ]
