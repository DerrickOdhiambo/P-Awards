# Generated by Django 3.1.2 on 2020-10-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rate',
        ),
        migrations.AddField(
            model_name='rating',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='content',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='design',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='usability',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
    ]