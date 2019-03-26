"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.conf.urls import path
from django.contrib import admin
from django.urls import path
from store_time import views
from django.views.generic import TemplateView
# from django.urls import url , include


# urlpatterns = patterns('',
#     url(r'^$','store_time.views.index',name='home'),
#     url(r'^admin/',include(admin.sites.urls)),
#     )


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', 
        TemplateView.as_view(template_name = 'about.html'), name='about'),
    path('contact/',
        TemplateView.as_view(template_name='contact.html'),name='contact'),
    path('results/',
        TemplateView.as_view(template_name='results.html'),name='results'),
    path('admin/', admin.site.urls),
]
