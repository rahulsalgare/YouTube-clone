from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Video
# from django.forms import Textarea

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

class React(forms.Form):
    comment = forms.CharField(label="Comment", widget=forms.Textarea(attrs={'cols':115,'rows':5}))
