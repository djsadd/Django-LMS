from celery import shared_task
from django.contrib.auth import get_user_model
from core.utils import send_html_email
from django.conf import settings

from django.core.mail import send_mail


@shared_task
def send_new_student_email(user_pk, password):
    print("NEW")
    user = get_user_model().objects.get(pk=user_pk)
    subject = "Your Dj LMS account confirmation and credentials"
    message = f'Thank you for registering at My Site.user: {user}, password: {password}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], )


@shared_task
def send_new_lecturer_email(user_pk, password):
    print("NEW")
    user = get_user_model().objects.get(pk=user_pk)
    subject = "Your Dj LMS account confirmation and credentials"
    message = f'Thank you for registering at My Site.user: {user}, password: {password}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], )
