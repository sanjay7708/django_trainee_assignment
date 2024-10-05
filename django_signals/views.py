import threading
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse

def trigger_signal(request):
    print(f"Signal trigger start: {now()}")
    print(f"Signal sender thread: {threading.get_ident()}")

    try:
        # Use a transaction block
        with transaction.atomic():
            # Trigger the signal by saving a User instance
            user = User.objects.create(username="testuser")
            print("Transaction will be rolled back")
            raise Exception("Force rollback")  # Force rollback to test transaction behavior
    except Exception as e:
        print(e)

    # Check if the user was saved after rollback
    user_exists = User.objects.filter(username="testuser").exists()
    print(f"User exists after rollback: {user_exists}")

    print(f"Signal trigger end: {now()}")
    return HttpResponse("Signal triggered")
