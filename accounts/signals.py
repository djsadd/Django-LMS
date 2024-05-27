from .tasks import send_new_student_email, send_new_lecturer_email
from .utils import generate_student_credentials, generate_lecturer_credentials


def post_save_account_receiver(sender, instance=None, created=True, *args, **kwargs):
    """
    Send email notification
    """
    print("created", created)
    if created:
        if instance.is_student:
            print("STUDENT")
            username, password = generate_student_credentials()
            instance.username = username
            instance.set_password(password)
            instance.save()
            # Send email with the generated credentials
            send_new_student_email(instance.pk, password)

        if instance.is_lecturer:
            username, password = generate_lecturer_credentials()
            instance.username = username
            instance.set_password(password)
            instance.save()
            # Send email with the generated credentials
            send_new_lecturer_email(instance.pk, password)
