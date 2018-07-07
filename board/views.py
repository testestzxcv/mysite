from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board
from board.models import User

# Create your views here.

def writeform(request):
    # 인증 체크
    if request.session['author'] is None:
        return HttpResponseRedirect('/user/loginform')

def view(request):
    id = request.GET['id']
    board_view = Board.objects.get(id=id)
    Board.objects.filter(id=id).update(hit=Board.objects.get(id=id).hit + 1)
    context = {'board_view' : board_view}

    return render(request, 'board/view.html', context)


def write(request):
    return render(request, 'board/write.html')

def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}
    return render(request, 'board/list.html', context)

def add(request):
    board = Board()
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.user_id = request.session['authuser']['id']
    board.name = request.session['authuser']['name']

    board.save()
    return HttpResponseRedirect('/board')

def deleteform(request):
    id = request.GET.get('id',False)
    context = {'id':id}
    return render(request, 'board/deleteform.html', context)

def delete(request):
    id = request.POST['no2']
    Board.objects.filter(id=id).delete()

    return HttpResponseRedirect('/board')

def modifyform(request):
    id = request.GET['id']
    board_view = Board.objects.get(id=id)
    context = {'board_view': board_view}

    return render(request, 'board/modifyform.html', context)

def modify(request):
    id = request.POST.get('id')
    board_save = Board.objects.get(id=id)
    board_save.title = request.POST['title']
    board_save.content = request.POST['content']
    board_save.save()

    return HttpResponseRedirect('/board/view?id='+id)

def search(request):
    return render(request, 'board/search.html')