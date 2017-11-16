from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^message$', views.add_message),
    url(r'^message/(?P<m_id>\d)/comment', views.post_comment)
]