from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.addr_list, name='addr_list'),
    url(r'addr/(?P<pk>\d+)/$', views.addr_detail, name='addr_detail'),
    url(r'addr/(?P<pk>\d+)/edit$', views.addr_edit, name='addr_edit'),
    url(r'addr/(?P<pk>\d+)/openaddr$', views.addr_openaddr, name='addr_openaddr'),
    url(r'addr/(?P<pk>\d+)/noopenaddr$', views.addr_noopenaddr, name='addr_noopenaddr'),
    url(r'addr/(?P<pk>\d+)/remove$', views.addr_remove, name='addr_remove'),
    url(r'addr/new/$', views.addr_new, name='addr_new'),
]