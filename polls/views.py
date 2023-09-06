from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from polls.models import Question

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView, TemplateView

# Create your views here.


print()

def index(request):
    # return HttpResponse("Olá... seja bem vindo a enquete")
    context = {'título': 'Página principal'}
    return render(request, "polls/home.html", context)


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
    template_name = 'polls/question_form.html'
    fields = ('question_text', 'pub_date', )
    success_url = reverse_lazy('polls_list')
    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Criando uma pergunta'
        return context

class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'polls/question_form.html'
    fields = ('question_text', 'pub_date', )
    success_url = reverse_lazy('polls_all')
    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Editando a pergunta'
        return context

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'polls/question_confirm_delete_form.html'
    success_url = reverse_lazy('polls_list')
    success_message = 'Pergunta excluída com sucesso.' 
    
    # implementa o método que conclui a ação com sucesso
    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(QuestionDeleteView, self).form_valid(request, *args, **kwargs)

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/question_detail.html'
    context_object_name = 'question'

class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'
    context_object_name = 'questions'
    paginate_by = 5 # quantidade de itens por página
    ordering = ['-pub_date'] # ordenar pela data de publicação de forma inversão

class SobreTemplateView(TemplateView):
    template_name = 'polls/sobre.html'

