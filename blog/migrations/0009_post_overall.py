# Generated by Django 3.0.8 on 2020-10-08 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='overall',
            field=models.IntegerField(default=0),
        ),
    ]
