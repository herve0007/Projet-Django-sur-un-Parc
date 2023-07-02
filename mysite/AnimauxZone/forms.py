from django import forms
from .models import Animaux, ZoneCoeur


class AnimauxForm(forms.ModelForm):
    class Meta:
        model= Animaux
        fields=('zoneCoeur', 'espece','famille', 'texte', 'image')


class ZoneForm(forms.ModelForm):
    class Meta:
        model= ZoneCoeur
        fields=('nom', 'superficie', 'x', 'y')
