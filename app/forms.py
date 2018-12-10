from django.forms import Form
from django import forms


class NoteForm(Form):
    name = forms.CharField()
    message = forms.CharField()
