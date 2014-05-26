from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.contrib.auth import login
from manozodynas.models import Word
from manozodynas.models import Translation
from django.views.generic import CreateView

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    #import ipdb; ipdb.set_trace()
    return render(request, 'manozodynas/login.html', {'form':form})

def words_view(request):
    return render(request, 'manozodynas/list.html', {'list':Word.objects.all()})

class TypeWord(CreateView):
    model = Word
    template_name = 'manozodynas/type_word.html'
    success_url = '/list_words/'

class TypeTranslation(CreateView):
    model = Translation
    template_name = 'manozodynas/type_translation.html'
    success_url = '/list_words/'

    def get_context_data(self, **kwargs):
        sarasas=super(TypeTranslation, self).get_context_data(**kwargs)
        a=self.kwargs.get("pk")
        sarasas["pk"]=a
        zod=Word.objects.get(pk=a)
        sarasas["var"]=zod
        return sarasas
