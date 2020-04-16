from django import forms
from .models import Server

class NewServerForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The name of the server'}), max_length=100)
    Path = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The path to the LGSM script'}), max_length=200)
    Port = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'The port to of the server'}))
    IP = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'placeholder': 'The IP of the server'}))

    class Meta:
        model = Server
        fields = ['Name', 'Path', 'IP', 'Port']