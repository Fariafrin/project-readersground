from django.urls import *
from . import views

urlpatterns=[
    path('upload/', views.upload, name="upload"),
    path('show/', views.show, name="show"),
    path('update/<int:pid>/', views.update, name='update'),
    path('delete/',views.delete, name='delete'),
]
