from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login),
	url(r'^index$', views.index),
	url(r'^sobre$', views.sobre),
	url(r'^cadastro$', views.cadastro),
	url(r'^cadastro2$', views.cadastro2),
	url(r'^login$', views.login),
	url(r'^produto$', views.produto)
]