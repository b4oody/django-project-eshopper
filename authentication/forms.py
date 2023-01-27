
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            self.user = User.objects.get(username=username)
        except  User.DoesNotExist:
            raise forms.ValidationError(f'The user with username {username} does not exist')

        if not self.user.check_password(password):
            raise forms.ValidationError(f'Password for user {username} is not correct!')




class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ('The two password fields didn’t match.'),
        'password_min': ('The entered password is too short. It must contain at least 8 characters.')
    }

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-register', 'placeholder': 'Smith'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-register', 'placeholder': 'smith@gmail.com'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-register', 'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-register', 'placeholder': 'Confirm password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            username = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(f'{username} already exists. Please try again.')

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(f"{email} is taken")
        return email

    def clean_password(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )

        return password2

















