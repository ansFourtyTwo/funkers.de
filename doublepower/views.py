from django.shortcuts import render, redirect

from .forms import PlayerForm, ExistingTeamPlayerForm
from .models import Team


def home(request):
    return render(
        request,
        'doublepower/home.html',
        {'player_form': PlayerForm()}
    )


def new_team(request):
    player_form = PlayerForm(data=request.POST)
    if player_form.is_valid():
        team = Team.objects.create()
        player_form.save(team=team)
        return redirect(team)


def view_team(request, team_id):
    team = Team.objects.get(pk=team_id)
    form = ExistingTeamPlayerForm(team=team)

    if request.method == 'POST':
        form = ExistingTeamPlayerForm(team=team, data=request.POST)
        if form.is_valid():
            form.save(team=team)
            return redirect(team)

    return render(
        request,
        'doublepower/team.html',
        {
            'team': team,
            'player_form': form,
         }
    )
