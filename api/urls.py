from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("auth/", include("authentication.urls", namespace="authentication")),
    path("support/", include("support.urls", namespace="support")),
    path("jobs/", include("jobs.urls", namespace="jobs")),
    path("settings/", include("settings.urls", namespace="settings")),
]
