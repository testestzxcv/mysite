from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook
# Create your views here.


def deleteform(request):
    id = request.GET.get('id',False)
    context = {'id':id}
    return render(request, 'guestbook/deleteform.html', context)

def delete(request):
    id = request.POST['no']
    password = request.POST['password']
    Guestbook.objects.filter(id=id).filter(password=password).delete()

    return HttpResponseRedirect('/guestbook')


def list(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/list.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.message = request.POST['message']

    guestbook.save()
    return HttpResponseRedirect('/guestbook')

