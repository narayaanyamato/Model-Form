from django import forms
from modelformapp.models import Movie
class Movieform(forms.ModelForm):
    title=forms.CharField()
    rating=forms.IntegerField()
    cast=forms.CharField()
    release=forms.CharField()
    gener=forms.CharField()
    class Meta:
        model= Movie
        fields='__all__'
