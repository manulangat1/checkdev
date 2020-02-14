from django.test import TestCase
from .models import Project,Review
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest
# unit tests
class ProjectTestCase(TestCase):
    def setUp(self):
        self.image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        self.manu = Project(title='manu',desc='mdmd',github_link='https://github.com/manulangat1',
        deployed_link='https://github.com/manulangat1',image=self.image)
    def test_instance(self):
        self.asssertTrue(isinstance(self.manu,Project))
