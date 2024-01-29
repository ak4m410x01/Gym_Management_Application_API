from django.urls import path, include

from .account import urlpatterns as account_urls
from .admin import urlpatterns as admin_urls
from .coach import urlpatterns as coach_urls
from .member import urlpatterns as member_urls
from .visitor import urlpatterns as visitor_urls


urlpatterns = [
    path("", include(account_urls)),
    path("admins/", include(admin_urls)),
    path("coaches/", include(coach_urls)),
    path("members/", include(member_urls)),
    path("visitors/", include(visitor_urls)),
]
