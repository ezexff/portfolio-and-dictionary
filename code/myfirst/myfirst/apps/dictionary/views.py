from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.urls import reverse

from .models import Dictionary, Comment, Card

from .forms import CardForm

# Вызываемые методы при переходе на страницу

def cards(request):
    error = ''
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена неверно'
    
    form = CardForm()

    latest_cards_list = Card.objects.order_by('-pub_date')[:5]

    data = {
        'form': form,
        'error': error,
        'latest_cards_list': latest_cards_list
    }
    return render(request, 'dictionary/cards.html', data)

#def add_card(request):
#    c = Card(word = request.POST['word'], definition = request.POST['definition'])
#    c.save()
#    return HttpResponseRedirect(reverse('dictionary:cards'))

def index(request):
    latest_dictionary_list = Dictionary.objects.order_by('-pub_date')[:5]
    return render(request, 'dictionary/list.html', {'latest_dictionary_list' : latest_dictionary_list})

def detail(request, dictionary_id):
    try:
        d = Dictionary.objects.get(id = dictionary_id)
    except:
        raise Http404("Статья не найдена!")

    latest_comments_list = d.comment_set.order_by('-id')[:10]

    return render(request, 'dictionary/detail.html', {'dictionary': d, 'latest_comments_list': latest_comments_list})

def leave_comment(request, dictionary_id):
    try:
        d = Dictionary.objects.get(id = dictionary_id)
    except:
        raise Http404("Статья не найдена!")

    d.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('dictionary:detail', args = (d.id,)))
