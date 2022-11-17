from apps.profiles.models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["timezone", "image", "theme"]
        widgets = {"image": forms.FileInput()}
