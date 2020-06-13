from django.shortcuts import render

from .forms import PlayerForm


def home(request):
    return render(
        request,
        'doublepower/home.html',
        {'player_form': PlayerForm()}
    )
