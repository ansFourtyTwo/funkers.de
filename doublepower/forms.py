from django import forms

from doublepower.models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'forehand_strength', 'backhand_strength',)
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Please enter a player name'
            })
        }
