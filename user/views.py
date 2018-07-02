from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def joinform(request):
    return render(request, 'user/joinform.html')

def join(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save()

    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def loginform(request):
    return render(request, 'user/loginform.html')

def login(request):
    result = User.objects.filter(email=request.POST['email']).filter(password=request.POST['password']) # 한개가 아니라 리스트 비슷하게 들어온다. 리스트가 비어있으면 에러가 난다.

    # 로그인 실패
    if len(result) == 0:
        return HttpResponseRedirect('/user/loginform?result=false')

    # 로그인 처리
    authuser = result[0]
    request.session['authuser'] = model_to_dict(authuser)  # 인증처리
    # return HttpResponse('hello world')  # 텍스트를 출력하고 싶을때 /hello world 출력됨
    return HttpResponseRedirect('/')


def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')



