from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.


print()

def index(request):
    # return HttpResponse("Olá... seja bem vindo a enquete")
    context = {'título': 'Página principal'}
    return render(request, "home.html", context)


def sobre(request):
    return HttpResponse("Este é um app de enquete!")

def exibe_questao(request, question_id):
    questao = Question.objects.get(id=question_id)
    return HttpResponse(questao.question_text)

def ultimas_perguntas(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/perguntas.html', context)


class QuestionCreateView(CreateView):
    model = Question
    fields = ('question_text', 'pub_date')
    sucesss_url: reverse_lazy('index')


