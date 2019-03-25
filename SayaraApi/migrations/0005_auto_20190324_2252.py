# Generated by Django 2.1.7 on 2019-03-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SayaraApi', '0004_auto_20190324_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomOption', models.CharField(max_length=255)),
                ('codeOption', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AlterField(
            model_name='modele',
            name='couleurCompatible',
            field=models.ManyToManyField(blank=True, related_name='modeles', to='SayaraApi.Couleur'),
        ),
        migrations.AddField(
            model_name='version',
            name='optionsVersion',
            field=models.ManyToManyField(blank=True, related_name='versions', to='SayaraApi.Option'),
        ),
    ]
