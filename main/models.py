from django.db import models

# Create your models here.
class Mentor(models.Model):
    """Mentor object for Mentors"""
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=50)
    stack = models.CharField(max_length=150)
    dob = models.DateField(editable=True)
    image = models.ImageField(upload_to="images/mentors")



class Mentee(models.Model):
    """Mentee object for Mentees"""
    irst_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=50)
    stack = models.CharField(max_length=150)
    dob = models.DateField(editable=True)
    mentor = models.OneToOneField(Mentor, on_delete=models.RESTRICT, related_name="mentor", blank=True)
    image = models.ImageField(upload_to="images/mentees")

    def change_mentor(self, new_mentor = None):
        """method for changing the mentor of a mentee"""
        if new_mentor is not None:
            self.mentor = new_mentor