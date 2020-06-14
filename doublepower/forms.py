from django import forms

from doublepower.models import Player


class PlayerForm(forms.ModelForm):

    def save(self, team):
        self.instance.team = team
        return super().save(self)

    class Meta:
        model = Player
        fields = ('name', 'forehand_strength', 'backhand_strength',)
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Please enter a player name'
            }),
            'forehand_strength': forms.fields.NumberInput(attrs={
                'min': 0,
                'max': 100,
                'step': 1,
            }),
            'backhand_strength': forms.fields.NumberInput(attrs={
                'min': 0,
                'max': 100,
                'step': 1,
            })
        }


class ExistingTeamPlayerForm(PlayerForm):

    def __init__(self, team, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.team = team




