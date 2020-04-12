from django import forms
from webpanel.models import Server

class NewServerForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The name of the server'}), max_length=100)
    IP = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'placeholder': 'The IP of the server'}), protocol='IPv4')
    Port = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'The port of the server'}))
    User = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The name of the system user'}), max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'The password of the system user'}), max_length=100)

    class Meta:
        model = Server
        fields = ['Name', 'IP', 'Port', 'User', 'Password']