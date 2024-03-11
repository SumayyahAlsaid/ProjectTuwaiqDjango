from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        labels = {
            'username': 'اسم المستخدم',
            'email': 'البريد الالكتروني',
            'password1': 'Iكلمة المرور',
            'password2': 'تأكيد كلمة المرور',
        }

class LoginUserForm(AuthenticationForm):
    class Meta:
        model=User
        fields=('username','password')
        labels = {
            'username': 'اسم المستخدم',
            'password': 'كلمة المرور',
        }
        