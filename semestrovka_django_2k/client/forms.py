from django.forms import ModelForm

from client.models import UserProfile


class ChangeImage(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
