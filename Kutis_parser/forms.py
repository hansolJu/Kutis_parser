from django import forms

from parser_core.models import Student


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ['hukbun', 'password']