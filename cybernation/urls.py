"""cybernation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from finalp import views
urlpatterns = [
    path('admin/', admin.site.urls),url(r'^$', views.home, name='home'),
    path('owasp_homepage', views.owasp_homepage, name='owasp_homepage'),
    path('one', views.one, name='one'),
    path('two', views.two, name='two'),
    path('three', views.three, name='three'),
    path('four', views.four, name='four'),
    path('five', views.five, name='five'),
    path('six', views.six, name='six'),
    path('seven', views.seven, name='seven'),
    path('eight', views.eight, name='eight'),
    path('nine', views.nine, name='nine'),
    path('ten', views.ten, name='ten'),
    path('form', views.form, name='form'),
    path('netizens', views.netizens, name='netizens'),
    path('login', views.login, name='login'),
    

]
