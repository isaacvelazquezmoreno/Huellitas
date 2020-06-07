from django import forms

# Create your forms here.

class FormLogin(forms.Form):
    
    email = forms.EmailField()
    password = forms.PasswordInput()