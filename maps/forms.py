from django import forms
from .models import UserLocationModel


class UserLocationForm(forms.ModelForm):
    class Meta:
        model = UserLocationModel
        fields = "__all__"


