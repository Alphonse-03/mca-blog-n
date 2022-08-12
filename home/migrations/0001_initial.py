# Generated by Django 3.0.8 on 2020-09-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=500)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]