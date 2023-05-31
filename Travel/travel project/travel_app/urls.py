from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
   # path('another/',views.another,name='another'),
   # path('inner/',views.inner,name='inner')

]
