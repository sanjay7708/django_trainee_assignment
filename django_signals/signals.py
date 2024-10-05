import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.db import connection
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, created, **kwargs):
    # Synchronous behavior check with time delay
    print(f"Signal handler start: {now()}")
    time.sleep(3)  # Simulate delay
    print(f"Signal handler end: {now()}")

    # Thread check
    print(f"Signal handler thread: {threading.get_ident()}")

    # Database transaction check
    if created:
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM auth_user WHERE username = %s", [instance.username])
        result = cursor.fetchone()
        print(f"User in DB (within signal): {result}")
