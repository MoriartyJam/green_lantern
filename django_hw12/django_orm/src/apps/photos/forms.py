from django import forms
from apps.photos.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['car', 'image']
