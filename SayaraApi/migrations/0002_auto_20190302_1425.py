# Generated by Django 2.1.7 on 2019-03-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SayaraApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marque',
            name='idMarque',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
