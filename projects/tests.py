from django.test import TestCase
from .models import Project, Profile, User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Derrick')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()


class ProjectTest(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(username='Derrick')
        self.new_project = Project.objects.create(
            title='project1', project_description='testing project', project_owner='Derrick', project_link='https//:test.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def test_save_post(self):
        self.new_project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_get_posts(self):
        self.new_project.save()
        projects = Projects.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Project.search_by_title('test')
        self.assertTrue(len(post) > 0)
