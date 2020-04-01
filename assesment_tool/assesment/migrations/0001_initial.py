# Generated by Django 3.0.4 on 2020-03-31 15:46

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_id', models.IntegerField()),
                ('region', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('text', models.CharField(max_length=1000)),
                ('yes', models.CharField(max_length=50)),
                ('no', models.CharField(max_length=50)),
            ],
        ),
    ]
