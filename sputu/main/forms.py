from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import HomeworkSubmission

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


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    username = forms.CharField(
        label="Логин",  # <- Новый текст
        help_text="",  # <- Убираем описание
        max_length=150
    )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

class HomeworkSubmissionForm(forms.ModelForm):
    class Meta:
        model = HomeworkSubmission
        fields = ('file',)