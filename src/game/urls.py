from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("start/", views.start_view, name="start"),      # exemplo
    path("state/", views.state_view, name="state"),      # exemplo
    path("roll/", views.roll_view, name="roll"),         # exemplo
    path("battle/", views.battle_view, name="battle"),   # exemplo
]
