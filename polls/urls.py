from django.urls import path

from polls.models import Question

from . import views

urlpatterns =  [
    path('', views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"), 
    path("perguntas/", views.ultimas_perguntas, name='ultimas_perguntas'),
    path('cadastrar/', views.QuestionCreateView.as_views(), name="question-create")
]