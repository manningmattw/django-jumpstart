# Generated by Django 5.0.7 on 2024-07-31 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='choice',
            field=models.SmallIntegerField(choices=[(0, ''), (1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th')], default=1),
        ),
    ]