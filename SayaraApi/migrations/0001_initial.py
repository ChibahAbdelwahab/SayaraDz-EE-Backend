# Generated by Django 2.1.7 on 2019-03-21 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('idAnnonce', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=50)),
                ('prix', models.IntegerField()),
                ('commentaites', models.CharField(max_length=255)),
                ('idUser', models.ForeignKey(on_delete='DO_NOTHING', related_name='proprietaire', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricant',
            fields=[
                ('nomFabricant', models.CharField(max_length=255)),
                ('idFabricant', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('idMarque', models.AutoField(primary_key=True, serialize=False)),
                ('nomMarque', models.CharField(max_length=50)),
                ('imageMarque', models.ImageField(upload_to='marque/images/')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Modele',
            fields=[
                ('idModele', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nomModele', models.CharField(max_length=255)),
                ('marqueModele', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modeles', to='SayaraApi.Marque')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('numChassis', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('disponible', models.BooleanField()),
                ('imageVehicle', models.ImageField(default='images/vehicules/voiture.jpg', upload_to='images/vehicules')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('nomVersion', models.CharField(max_length=100)),
                ('codeVersion', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('modeleVersion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='SayaraApi.Modele')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AddField(
            model_name='vehicule',
            name='versionVoiture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicules', to='SayaraApi.Version'),
        ),
        migrations.AddField(
            model_name='fabricant',
            name='marqueFabricant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fabricants', to='SayaraApi.Marque'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='idVehicule',
            field=models.ForeignKey(on_delete='DO_NOTHING', related_name='vehicule', to='SayaraApi.Vehicule'),
        ),
    ]
