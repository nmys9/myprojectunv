from django.urls import path
from myappunv import views


urlpatterns = [
    path('get',views.get_fingerprint),
    path('post',views.post_fingerprint),
]
