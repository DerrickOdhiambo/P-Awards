from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from projects.models import Rating, RATE_CHOICES, Profile
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'user_bio']


class RatingForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(), required=False)
    rate = forms.ChoiceField(choices=RATE_CHOICES,
                             widget=forms.Select(), required=True)

    class Meta:
        model = Rating
        fields = ['rate', 'review']
