from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'phone_num', 'linkedin_url', 'profile_image')#forumda bu melumatlar bize gorunecek