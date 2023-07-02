# Generated by Django 4.2.1 on 2023-06-25 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZoneCoeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('superficie', models.IntegerField()),
                ('x', models.DecimalField(decimal_places=2, max_digits=15)),
                ('y', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Animaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espece', models.CharField(max_length=50)),
                ('famille', models.CharField(max_length=50)),
                ('texte', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='image')),
                ('zoneCoeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimauxZone.zonecoeur')),
            ],
        ),
    ]
