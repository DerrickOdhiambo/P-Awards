# Generated by Django 3.1.2 on 2020-10-28 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20201028_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='projects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_ratings', to='projects.project'),
        ),
    ]