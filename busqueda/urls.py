from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.search, name='search'),
		url(r'^$', views.base, name='base'),
        url(r'^$', views.porcentaje, name='porcentaje'),
        url(r'^$', views.count_codon, name='count_codon'),
        url(r'^$', views.count_base, name='count_base'),
        url(r'^$', views.total_base, name='total_base'),
    ]