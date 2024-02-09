from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail as mail
from celery import shared_task


@shared_task
def send_mail(
    subject: str = "",
    body: str = "",
    send_from: str = EMAIL_HOST_USER,
    send_to: list[str] = [],
) -> bool:
    return mail(subject, body, send_from, send_to)
