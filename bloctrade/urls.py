"""bloctrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from loginApp import authenticationAPI,calculator
from loginApp import groups

# urlpatterns = [
    # url(r'^admin/', admin.site.urls),
urlpatterns = [

    url(r'^signup/$', authenticationAPI.authentication.as_view(),name='signup'),
    url(r'^logout/$', authenticationAPI.logout.as_view(),name='logout'),
    url(r'^calculator/$', calculator.calculate.as_view(),name='calculator'),

    url(r'^conservativeGroup/$', groups.getConservativeGroup.as_view(),name='conservativeGroup'),
    url(r'^moderateGroup/$', groups.getModerateGroup.as_view(),name='moderateGroup'),
    url(r'^aggressiveGroup/$', groups.getAggressiveGroup.as_view(),name='aggressiveGroup'),
    url(r'^userGroup/$', groups.getUserGroup.as_view(),name='userGroup'),

]
