from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.default),
    url(r'^signin$', views.signin),
    url(r'^signin/process',views.signin_p),
    url(r'^register$', views.register),
    url(r'^register/process', views.register_p),
    url(r'^logoff$', views.signout)
]