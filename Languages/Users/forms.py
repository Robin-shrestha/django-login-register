from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"input100",'type':"text",'name':"username",'placeholder':"Username"}))
#     password = forms.CharField(widget=forms.TextInput(attrs={    'class':"input100",'type':"password",'name':"pass",'placeholder':"Password"}))

class RegisterForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)

    #     self.fields['username'].widget.attrs['class'] = 'input100'
    #     self.fields['email'].widget.attrs['class'] = 'input100'
    #     self.fields['password1'].widget.attrs['class'] = 'input100'
    #     self.fields['password2'].widget.attrs['class'] = 'input100'
