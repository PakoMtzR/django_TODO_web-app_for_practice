from django.urls import path
from . import views

urlpatterns = [path('', views.pending_list, name="pendings")]