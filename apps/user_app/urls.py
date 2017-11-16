from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^new$', views.add_new_user),
    url(r'^new/process$', views.add_new_user_p),
    url(r'^edit$', views.edit_user),
    url(r'^edit/process', views.edit_user_p),
    url(r'^edit/(?P<u_id>\d+)$', views.edit_user_by_id),
    url(r'^edit/(?P<u_id>\d+)/process$', views.edit_user_by_id_p),
    url(r'^show/(?P<u_id>\d+)$', views.show_user),
    url(r'^show/(?P<u_id>\d+)/post/', include('apps.msg_app.urls'))
]