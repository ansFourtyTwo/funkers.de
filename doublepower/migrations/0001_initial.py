# Generated by Django 3.0.7 on 2020-06-14 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('forehand_strength', models.IntegerField(default=50)),
                ('backhand_strength', models.IntegerField(default=50)),
                ('team', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='doublepower.Team')),
            ],
        ),
    ]
