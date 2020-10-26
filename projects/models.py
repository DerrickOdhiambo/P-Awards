from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField


class Project(models.Model):
    title = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='project/')
    project_description = models.TextField()
    project_link = models.CharField(max_length=60)
    project_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    @classmethod
    def all_images(cls):
        project_images = cls.objects.all()
        return project_images

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    profile_picture = ResizedImageField(size=[300, 300], quality=75,
                                        default='default.jpg', upload_to='profile_pics/')
    user_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


RATE_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
]


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    review = models.TextField()

    def __str__(self):
        return self.user.username
