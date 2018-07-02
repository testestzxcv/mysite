from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook
# Create your views here.

def list(request):
    guestbook_list = Guestbook.objects.all().order_by('regdate')
    context = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/list.html', context)

def deleteform(request):
    id = request.GET.get('id',False)
    context = {'id':id}
    return render(request, 'guestbook/deleteform.html', context)

def delete(request):
    id = request.POST['a']
    password = request.POST['password']
    Guestbook.objects.filter(id=id).filter(password=password).delete()


def add(request):
    guestbook = Guestbook()
    guestbook.id = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.content = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

