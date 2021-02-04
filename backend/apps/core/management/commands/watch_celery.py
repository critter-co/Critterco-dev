"""
This command allows for celery to be reloaded when project
code is saved. This command is called in
`docker-compose.dev.yml` and is only for use in development
https://gitlab.com/briancaffey/verbose-equals-true/-/blob/develop/documentation/README.md#celery-and-redis
https://avilpage.com/2017/05/how-to-auto-reload-celery-workers-in-development.html
"""

import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload  # noqa F401


def restart_celery():
    cmd = 'pkill -9 celery'
    subprocess.call(shlex.split(cmd))
    cmd = 'celery worker --app=backend.celery_app:app --loglevel=info'
    subprocess.call(shlex.split(cmd))


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Starting celery worker with autoreload...')
        try:
            # autoreload.main(inner_run)
            from django.utils.autoreload import run_with_reloader
            run_with_reloader(restart_celery)
        except ImportError:
            from django.utils import autoreload  # noqa F811
            autoreload.main(restart_celery)
        # autoreload.main(restart_celery)
