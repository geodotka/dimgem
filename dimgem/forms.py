from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class SearchingForm(forms.Form):
    word = forms.CharField(label='Wpisz szukaną frazę')


class RegisterForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(
        label='hasło',
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(6)],
        error_messages={'min_length': u'Hasło musi mieć co najmniej 6 znaków'}
    )

    password2 = forms.CharField(
        label='powtórz hasło', widget=forms.PasswordInput)
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput)

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if User.objects.filter(username=login):
            raise forms.ValidationError(u'Podany login istnieje w bazie')
        return login

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError(u'Podane hasła nie są zgodne')
        return password2


class LoginForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(label='hasło', widget=forms.PasswordInput)

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if not User.objects.filter(username=login):
            raise forms.ValidationError(u'Podany login nie istnieje w bazie')
        return login
