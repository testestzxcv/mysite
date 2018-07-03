from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board
from board.models import User

# Create your views here.

def writeform(request):
    # 인증 체크
    if request.session['author'] is None:
        return HttpResponseRedirect('/user/loginform')

def write(request):
    return render(request, 'board/write.html')

def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}
    return render(request, 'board/list.html', context)

def add(request):
    result = User.objects.filter(name=request.POST['name'])
    print("result=========", result[0])
    board = Board()
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.hit += 1
    board.user = result[0]

    board.save()
    return HttpResponseRedirect('/board')