from django.db import models
from django.utils.timezone import now


class Project(models.Model):
    title = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='project/')
    project_description = models.TextField()
    project_link = models.CharField(max_length=60)
    project_owner = models.CharField(max_length=30)
    date_posted = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
