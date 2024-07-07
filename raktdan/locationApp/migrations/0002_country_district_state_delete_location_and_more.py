# Generated by Django 5.0.6 on 2024-07-07 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('country_code', models.CharField(default='+91', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DistrictCountry', to='locationApp.country')),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DistrictCountryCode', to='locationApp.country')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StateCountry', to='locationApp.country')),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StateCountryCode', to='locationApp.country')),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DistrictState', to='locationApp.state'),
        ),
    ]
