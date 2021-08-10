from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import mail
from django.conf import settings
from .models import ContactMessage


@receiver(post_save, sender=ContactMessage)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        mail.send_mail('contact message', instance.message+"\nsender:"+instance.email,
                       settings.EMAIL_ADDRESS, [settings.ADMIN_EMAIL], True)
