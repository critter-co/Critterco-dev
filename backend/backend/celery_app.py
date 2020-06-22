import os
import time
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery import shared_task
from celery import Celery
from django.core.mail import EmailMultiAlternatives

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Doing async task")
    time.sleep(2)
    print("Task is done")


@shared_task
def send_email_task(*args, **kwargs):
    user_mail = kwargs['email']
    send_mail(
        'Activate Your Account',
        'Here is the activation code: %s' % args,
        'hoseyn.wanton@gmail.com',
        [user_mail]
    )


@shared_task
def send_htmail_task(*args, **kwargs):
    user_mail = kwargs['email']
    code = args[0]
    msg = EmailMultiAlternatives(
        subject="Please activate your account",
        body="Here is the activation code: %s" % code,
        from_email="hoseyn.wanton@gmail.com",
        to=[user_mail],
        reply_to=["hoseyn.wanton@gmail.com"])

    msg_html = render_to_string('emails/account_activation.html', {'code': code})
    msg.attach_alternative(msg_html, "text/html")

    # Send it:
    msg.send()
