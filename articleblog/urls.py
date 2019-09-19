"""articleblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('about/',views.about),
    path('listpic/',views.listpic),
    path('newslistpic/',views.newslistpic),
    path('base/',views.base),
    path('addarticle/',views.addarticle),
    path('fytest/',views.fytest),
    path('newslistpic/', views.newslistpic),
    re_path('newslistpic/(?P<page>\d+)',views.newslistpic),
    re_path('textcontent/(?P<id>\d+)',views.textcontent),
    # path('Article/',include('Article.urls'))
    path('sexceshi/',views.sexceshi),
    path('request/',views.request),
    path('formtest/',views.formtest),
    path('register/',views.register),
    path('ajax_get/',views.ajax_get),
    path('ajax_get_data/',views.ajax_get_data),
    path('ajax_post/',views.ajax_post),
    path('ajax_post_data/',views.ajax_post_data),
    path('checkusername/',views.checkusername),
    path('login/',views.login),
    path('ajax_gets/',views.ajax_gets),
    path('ajax_gets_data/',views.ajax_gets_data),
    path('ajax_posts/',views.ajax_posts),
    path('ajax_posts_data/',views.ajax_posts_data),
    path('logout/',views.logout),
]
