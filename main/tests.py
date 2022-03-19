from django.test import TestCase
from .models import Mentee, Mentor
# Create your tests here.


class TestMentor(TestCase):

    def setUp(self) -> None:
        self.mentor = Mentor.objects.create()
        self.mentor.save()

    def test_model_is_created(self):
        return self.mentor.exists()