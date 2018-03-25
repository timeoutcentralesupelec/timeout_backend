from django.forms import forms


class eventForm(forms.ModelForm):
    link = forms.RegexField(regex=r'\w+')