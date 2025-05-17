from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='Эл. почта')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

    def send_email(self):
        send_mail(
            f'Сообщение с сайта от {self.cleaned_data["name"]}',
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )