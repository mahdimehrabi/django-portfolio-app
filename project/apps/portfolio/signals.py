from django.db.models.signals import post_save
from django.dispatch import  receiver
from .models import ContactMessage
from django.core import mail

@receiver(post_save,sender=ContactMessage)
def send_contact_email(sender,instance,created,**kwargs):
    if created:
        mail.send_mail('contact message',instance.message,settings.email)

