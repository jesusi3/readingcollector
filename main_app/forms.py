from django.forms import ModelForm
from .models import BookMark

class BookMarkForm(ModelForm):
    class Meta:
        model = BookMark
        fields = ['date', 'chapter']