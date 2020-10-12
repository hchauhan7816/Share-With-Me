from django.db.models.signals import post_save
from .models import Person
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_person_of_user(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
