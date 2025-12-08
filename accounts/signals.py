from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile_log(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.username} ({instance.role})")
