import os
import time
from django.core.mail import send_mail
from celery import shared_task
from celery import Celery

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
