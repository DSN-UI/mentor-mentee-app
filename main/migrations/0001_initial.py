# Generated by Django 4.0.3 on 2022-03-14 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.CharField(max_length=50)),
                ('stack', models.CharField(max_length=150)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irst_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.CharField(max_length=50)),
                ('stack', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('mentor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to='main.mentor')),
            ],
        ),
    ]