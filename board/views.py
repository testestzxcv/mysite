from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def writeform(request):
    # 인증 체크
    if request.session['author'] is None:
        return HttpResponseRedirect('/user/loginform')

def list(request):
    return render(request, 'board/list.html')

def write(request):
    return render(request, 'board/write.html')