from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('firstapp/',views.home,name='firstapp')
]
