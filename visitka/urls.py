"""visitka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import MemberUpdate, UserDelete
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.main', name='main'),
    url(r'^contact/$', 'myapp.views.contact', name='contact'),
    url(r'^accounts/register/$', 'myapp.views.register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^cabinet/edit/(?P<pk>\d+)/$', MemberUpdate.as_view(), name='member_update'),
    url(r'^cabinet/(?P<pk>[0-9]+)/delete/$', UserDelete.as_view(), name='user_delete'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)