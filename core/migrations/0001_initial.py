# Generated by Django 3.1.7 on 2021-05-18 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('kind', models.CharField(choices=[('APT', 'Advanced Persistent Threat'), ('CRI', 'CyberCrime'), ('HAK', 'Hacktivism'), ('KID', 'Opportunistic / ScriptKidies / Not directly targeted'), ('UNK', 'Unknown')], default='UNK', max_length=3)),
                ('aim', models.TextField(null=True)),
                ('TTPs', models.TextField(null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('criticality', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('kind', models.CharField(choices=[('IP', 'IP Address'), ('FQDN', 'Domain'), ('URL', 'URL path'), ('JA3', 'JA3/JA3S'), ('PROC', 'Process'), ('HIVE', 'Registry Key'), ('FILE', 'File or Folder'), ('HASH', 'HASH'), ('OTH', 'Other ...')], max_length=4)),
                ('status', models.CharField(choices=[('IOC', 'Malicious'), ('SUS', 'Suspicious'), ('RAS', 'Whitelisted')], default='SUS', max_length=3)),
                ('TTP', models.CharField(max_length=32, null=True)),
                ('comment', models.TextField(null=True)),
                ('actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.actor')),
            ],
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('kind', models.CharField(choices=[('WKS', 'Workstation'), ('SVR', 'Server'), ('NET', 'Networking Device'), ('OTH', 'Other'), ('UNK', 'Unkown')], default='UNK', max_length=3)),
                ('status', models.CharField(choices=[('COM', 'Compromised'), ('UNK', 'Unknown'), ('RAS', 'Healthy')], default='UNK', max_length=3)),
                ('function', models.CharField(max_length=32, null=True)),
                ('criticality', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1)),
                ('comment', models.TextField(null=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.area')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, null=True)),
                ('surname', models.CharField(max_length=32, null=True)),
                ('status', models.CharField(choices=[('COM', 'Compromised'), ('UNK', 'Unknown'), ('RAS', 'Healthy')], default='UNK', max_length=3)),
                ('function', models.CharField(max_length=32, null=True)),
                ('criticality', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1)),
                ('comment', models.TextField(null=True)),
                ('endpoint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='Corrupted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDetection', models.DateTimeField(auto_now_add=True)),
                ('dateBegin', models.DateTimeField(null=True)),
                ('dateEnd', models.DateTimeField(null=True)),
                ('artifact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.artifact')),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.endpoint')),
            ],
        ),
    ]
