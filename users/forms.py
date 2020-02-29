from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Request

class DateInput(forms.DateInput):
    input_type = 'date'
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('full_name','phone','parent_phone','gender')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('phone','parent_phone')

class UserOutingForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = [
            'from_user', 'assigned_to','when','return_date','place','purpose'
        ]
        widgets = {
            'when': DateInput(attrs={'type': 'date'}),
            'return_date': DateInput(attrs={'type': 'date'})
        }