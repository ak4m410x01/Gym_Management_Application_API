from django.urls import path, include
from settings.urls.aboutUs import urlpatterns as aboutUs_urls
from settings.urls.contactUs import urlpatterns as contactUs_urls

app_name = "settings"

urlpatterns = [
    path("about-us/", include(aboutUs_urls), name="about-us"),
    path("contact-us/", include(contactUs_urls), name="contact-us"),
]
