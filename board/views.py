from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board

# Create your views here.

def writeform(request):
    # 인증 체크
    if request.session['author'] is None:
        return HttpResponseRedirect('/user/loginform')

def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list':board_list}
    return render(request, 'board/list.html', context)

def write(request):
    return render(request, 'board/write.html')