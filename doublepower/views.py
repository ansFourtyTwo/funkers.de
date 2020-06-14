from django.shortcuts import render

from .forms import PlayerForm
from .models import Player


def home(request):
    return render(
        request,
        'doublepower/home.html',
        {'player_form': PlayerForm()}
    )


def new_player(request):
    player_form = PlayerForm(data=request.POST)
    if player_form.is_valid():
        player_form.save()
    return render(
        request,
        'doublepower/home.html',
        {'player_form': PlayerForm()}
    )
