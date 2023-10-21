from datetime import datetime, timezone
from users.models import User

from celery import shared_task


@shared_task
def deactivate_user():
    current_dt = datetime.now(timezone.utc)
    for user in User.objects.filter(is_active=True):
        if (current_dt - user.last_login) >= 120:
            user.is_active = False

