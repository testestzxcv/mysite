"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# [브라우저에서 입력한 url을 가져와서 이곳에서 함수를 실행한다]

from django.contrib import admin
from django.urls import path

import main.views as main_views
import user.views as user_views
import guestbook.views as guest_views
import board.views as board_views

urlpatterns = [
    path('', main_views.index),

    path('board/', board_views.list),
    path('board/write', board_views.write),
    path('board/add', board_views.add),
    path('board/view', board_views.view),

    path('guestbook/', guest_views.list),
    path('guestbook/add', guest_views.add),
    path('guestbook/deleteform/', guest_views.deleteform),
    path('guestbook/delete', guest_views.delete),

    path('user/joinform/', user_views.joinform),
    path('user/join', user_views.join),
    path('user/joinsuccess/', user_views.joinsuccess),
    path('user/loginform/', user_views.loginform),
    path('user/login', user_views.login),
    path('user/logout', user_views.logout),

    path('admin/', admin.site.urls),
]
