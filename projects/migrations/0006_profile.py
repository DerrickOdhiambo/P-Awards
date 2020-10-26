# Generated by Django 3.1.2 on 2020-10-26 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=75, size=[300, 300], upload_to='profile_pics/')),
                ('user_bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]