# Generated by Django 4.1.1 on 2022-12-06 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Vanue Name')),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100, verbose_name='Zip code')),
                ('phone', models.CharField(max_length=100, verbose_name='Contract')),
                ('website', models.URLField(max_length=100, verbose_name='Web address')),
                ('email_address', models.EmailField(max_length=100, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(auto_now_add=True)),
                ('manager', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('attendees', models.ManyToManyField(blank=True, to='event.user')),
                ('vanues', models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='event.venue')),
            ],
        ),
    ]