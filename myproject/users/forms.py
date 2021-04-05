from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from .models import Profile

username_validator = UnicodeUsernameValidator()
User._meta.get_field('email')._unique = True


class UserRegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("Aynı şifreyi girmediniz."),
    }
    username = forms.CharField(
        label=_('Kullanıcı Adı'),
        max_length=50,
        validators=[username_validator],
        error_messages={'unique': _("Bu isimde bir kullanıcı zaten mevcut.")},
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        max_length=64,
        widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(
        label=_('Şifre'),
        widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
        help_text=
        "Şifre en az 8 karakter olmalı ve sadece sayılardan oluşmamalıdır.",
    )
    password2 = forms.CharField(
        label=_('Şifre (Tekrar)'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_('Onaylamak için aynı şifreyi giriniz'))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Kullanıcı Adı',
                             widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=_("Şifre"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': _("Kullanıcı adı veya şifre yanlış."),
        'inactive': _("Bu hesap inaktiftir."),
    }


class UserUpdateForm(forms.ModelForm):
    username = UsernameField(
        label='Kullanıcı Adı',
        widget=forms.TextInput(attrs={'autofocus': True}),
        error_messages={'unique': _("Bu isimde bir kullanıcı zaten mevcut.")})
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label="Profil Resmini Güncelle",
                             widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['image']


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
