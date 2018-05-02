from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^feed/$', views.posts_list),
]
