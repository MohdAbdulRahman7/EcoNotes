# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from .models import Member
#
# User = get_user_model()
#
#
# @receiver(post_save, sender=User)
# def create_member(sender, instance, created, **kwargs):
#     if created and not instance.is_superuser:
#         # Check if the instance is already a Member to avoid recursion
#         if not isinstance(instance, Member):
#             Member.objects.create(
#                 username=instance.username,
#                 password=instance.password,
#                 email=instance.email,
#                 first_name=instance.first_name,
#                 last_name=instance.last_name,
#                 is_staff=instance.is_staff,
#                 is_active=instance.is_active,
#                 date_joined=instance.date_joined,
#                 last_login=instance.last_login
#             )
#
#
# @receiver(post_save, sender=User)
# def save_member(sender, instance, **kwargs):
#     if not instance.is_superuser and isinstance(instance, Member):
#         instance.save()


# signals.py
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Member


@receiver(post_save, sender=User)
def create_member_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'member'):
        Member.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_member_profile(sender, instance, **kwargs):
    if hasattr(instance, 'member'):
        instance.member.save()
