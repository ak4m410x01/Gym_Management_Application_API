from django.db import models
from settings.models.contactUs import ContactUs


class AboutUs(models.Model):
    the_face_of_your_business = models.TextField(
        max_length=20_000, blank=True, null=True
    )
    who_are_serve = models.TextField(max_length=20_000, blank=True, null=True)
    our_mission = models.TextField(max_length=20_000, blank=True, null=True)
    our_goals = models.TextField(max_length=20_000, blank=True, null=True)

    contact = models.OneToOneField(ContactUs, on_delete=models.CASCADE)
