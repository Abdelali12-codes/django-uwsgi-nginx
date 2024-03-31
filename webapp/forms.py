from django import forms

class NameForm(forms.Form):
    firstname = forms.CharField(label="firstname", required=True, max_length=20)
    lastname = forms.CharField(label="lastname", required=True, max_length=20)