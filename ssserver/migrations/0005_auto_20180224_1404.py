# Generated by Django 2.0 on 2018-02-24 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssserver', '0004_aliveip'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aliveip',
            options={'ordering': ['-log_time'], 'verbose_name_plural': '节点在线IP'},
        ),
    ]
