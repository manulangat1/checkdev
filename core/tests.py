from django.test import TestCase
from .models import Project,Review
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest
# unit tests
class ProjectTestClass(TestCase):
    def setUp(self):
        # self.image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        self.manu = Project(title='manu',desc='mdmd',github_link='https://github.com/manulangat1',
        deployed_link='https://github.com/manulangat1')
    def test_instance(self):
        self.assertTrue(isinstance(self.manu,Project))
    def test_save(self):
        self.manu.save()
        proj = Project.objects.all()
        self.assertTrue(len(proj) > 0)
