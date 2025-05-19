import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import TestModel

@receiver(post_save, sender=TestModel)
def signal_handler(sender, instance, **kwargs):
    print("Signal started")
    print("Same thread?", threading.get_ident())
    print("Inside transaction block?", transaction.get_connection().in_atomic_block)
    time.sleep(5)  # simulate long processing
    print("Signal ended")
