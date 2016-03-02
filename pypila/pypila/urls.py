"""pypila URL Configuration

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

from django.views.decorators.csrf import csrf_exempt
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(
        r'^api/czlonkowie_rodziny/$',
        csrf_exempt(views.CzlonkowieRodzinyAPIView.as_view())
        ),
    url(
        r'^api/czlonkowie_rodziny/(?P<pk>\d+)/$',
        csrf_exempt(views.CzlonkowieRodzinyAPIView.as_view())
    ),
    url(r'^hello_world/', views.HelloWorld.as_view()),
    url(r'^hello_name/(?P<name>\w+)', views.HelloName.as_view()),
    url(r'^czlonkowie_rodziny/', views.CzlonkowieRodziny.as_view()),
    url(r'^say_hello/', views.SayHello.as_view()),
    url(r'^czlonkowie_rodziny2/', views.WyszukajDodajCzlonka.as_view()),
#    url(r'^czlonkowie_rodziny', views.CzlonkowieRodziny.as_view())
#    url(r'^', views.hello_world),
#    url(r'^(?P<name>\w+)/', views.hello_name),
#    url(r'^(?P<id>\d+)/', views.hello_family),
]
