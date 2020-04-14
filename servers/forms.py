from django import forms
from webpanel.models import Server

class NewServerForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The name of the server'}), max_length=100)
    Path = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The path to the LGSM script'}), max_length=200)

    class Meta:
        model = Server
        fields = ['Name', 'Path']