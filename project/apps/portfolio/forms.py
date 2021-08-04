from django import forms
from .models import ContactMessage
from django.utils.translation import gettext_lazy as _

class ContactMessageForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':_('Your email')}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Your message')}))

    class Meta:
        model = ContactMessage
        fields = ['email', 'message']