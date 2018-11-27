from django.urls import path, re_path

from . import views

app_name = 'shjGuestbookUrl'

urlpatterns = [
    path('', views.index, name='index'),
    path('submitComment/', views.submitComment),
]
