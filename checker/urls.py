from django.conf.urls import url
from django.contrib import admin
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^plagiarism/',views.check,name = 'check'),
    url(r'^plagchecker',views.geturls,name='geturls'),
	url(r'^upload/$', views.model_form_upload, name='model_form_upload'),
	]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
