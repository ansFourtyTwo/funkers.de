"""double URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from . import views

app_name = 'doublepower'
urlpatterns = [
    path('', views.home, name='home'),
    path('team/new', views.new_team, name='new_team'),
    path('team/<int:team_id>', views.view_team, name='view_team'),
    path('team/<int:team_id>/player_up/<int:player_id>', views.player_up,
         name='player_up')
]
