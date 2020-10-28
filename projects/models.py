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

    def save_project(self):
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def all_images(cls):
        project_images = cls.objects.all()
        return project_images

    @classmethod
    def search_by_title(cls, project):
        projects = cls.objects.filter(title__icontains=project)
        return projects

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    profile_picture = ResizedImageField(size=[300, 300], quality=75,
                                        default='default.jpg', upload_to='profile_pics/')
    user_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()


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
    projects = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='project_ratings')
    design = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    content = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    usability = models.PositiveSmallIntegerField(
        choices=RATE_CHOICES, null=True)
    average_rating = models.FloatField(default=0)
    review = models.TextField()

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_ratings(cls, id):
        rating = cls.objects.all()[id]
        # return rating
        return [rating]
