# Generated by Django 2.1.7 on 2019-09-15 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SayaraApi', '0002_auto_20190915_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='client',
            new_name='user',
        ),
    ]
