from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class HelloForm(forms.Form):
    name    = forms.CharField(label='Your Name', max_length=100)
    email   = forms.EmailField(label='Your Email')