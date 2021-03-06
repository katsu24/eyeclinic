# Generated by Django 2.0.1 on 2018-01-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('pname', models.CharField(max_length=20)),
                ('pnamekana', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('psex', models.IntegerField(choices=[(0, 'Man'), (1, 'Woman')])),
                ('memo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('memo', models.TextField()),
            ],
        ),
    ]
