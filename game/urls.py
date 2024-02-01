from django.urls import path
from .views import NewGame, Turn

urlpatterns = [
    path('new', NewGame.as_view()),
    path('turn', Turn.as_view())
]
