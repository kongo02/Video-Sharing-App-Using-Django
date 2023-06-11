from django import forms
from . models import Video


class VideoUploadForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ["title", "creator", "description", "category", "video"]
