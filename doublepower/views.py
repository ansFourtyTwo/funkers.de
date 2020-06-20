from django.shortcuts import render, redirect

from .forms import PlayerForm, ExistingTeamPlayerForm
from .models import Team, Player


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
            form.save()
            return redirect(team)

    return render(
        request,
        'doublepower/team.html',
        {
            'team': team,
            'player_form': form,
         }
    )


def player_up(request, team_id, player_id):
    team = Team.objects.get(pk=team_id)

    upranked_player = Player.objects.get(pk=player_id)

    if not upranked_player.rank == 1:
        downranked_player = Player.objects.get(
            team=team,
            rank=(upranked_player.rank - 1)
        )
        upranked_player.rank -= 1
        downranked_player.rank += 1
        Player.objects.bulk_update(
            [upranked_player, downranked_player], ['rank']
        )

    return redirect(team)


def player_down(request, team_id, player_id):
    team = Team.objects.get(pk=team_id)

    downranked_player = Player.objects.get(pk=player_id)
    lowest_ranked_player = Player.objects.filter(team=team).last()

    if not downranked_player.rank == lowest_ranked_player.rank:
        upranked_player = Player.objects.get(
            team=team,
            rank=(downranked_player.rank + 1)
        )
        upranked_player.rank -= 1
        downranked_player.rank += 1
        Player.objects.bulk_update(
            [upranked_player, downranked_player], ['rank']
        )

    return redirect(team)
