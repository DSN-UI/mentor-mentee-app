from django.test import TestCase
from .models import Mentee, Mentor
# Create your tests here.
import datetime


class TestMentor(TestCase):

    def setUp(self) -> None:
        data = {
            "first_name": "Tomi",
            "last_name": "Ayo",
            "email": "ayo@gmail.com",
            "phone_number": "09091305248",
            "stack": "Backend",
            "dob": datetime.date(2000,3,21)

        }
        self.mentor = Mentor.objects.create(**data)
        self.mentor.save()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_model_is_created(self) -> bool:
        return self.mentor is not None

    def test_dob_exists(self) -> bool:
        dob = datetime.date(2000,3,21)
        m_dob = Mentor.objects.get(dob=dob)
        self.assertTrue(m_dob)