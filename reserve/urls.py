from django.conf.urls import url
from reserve import views

app_name = 'reserve'

urlpatterns = [
    url(r'^patient/$', views.patient_list, name='patient_list'),
    url(r'^patient/add/$', views.patient_edit, name='patient_add'),
    url(r'^patinet/mod/(?P<patient_id>\d+)/$', views.patient_edit, name='patient_mod'),
    url(r'^patient/del/(?P<patient_id>\d+)/$', views.patient_del, name='patient_del'),
    url(r'^reserve/$', views.reserve_list, name='reserve_list'),
    url(r'^reserve/add/$', views.reserve_edit, name='reserve_add'),
    url(r'^reserve/mod/(?P<reserve_id>\d+)/$', views.reserve_edit, name='reserve_mod'),
    url(r'^reserve/del/(?P<reserve_id>\d+)/$', views.reserve_del, name='reserve_del'),
]