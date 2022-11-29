from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:

        model= User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean_password2(self):
        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class UsearRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')