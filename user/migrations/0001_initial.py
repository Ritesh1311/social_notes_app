# Generated by Django 2.2.5 on 2020-01-25 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notesCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='userReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField()),
                ('password', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='sharedWith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_access', models.BooleanField(default=True)),
                ('edit_access', models.BooleanField(default=True)),
                ('notes_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.notesCreation')),
                ('shared_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userReg')),
            ],
        ),
        migrations.AddField(
            model_name='notescreation',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userReg'),
        ),
    ]