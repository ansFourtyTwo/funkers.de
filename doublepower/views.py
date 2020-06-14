from django.shortcuts import render, redirect

from .forms import PlayerForm
from .models import Player, Team


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


def new_team(request):
    player_form = PlayerForm(data=request.POST)
    if player_form.is_valid():
        team = Team.objects.create()
        return redirect(team)


def view_team(request, team_id):
    return render(
        request,
        'doublepower/team.html',
        {'player_form': PlayerForm()}
    )

