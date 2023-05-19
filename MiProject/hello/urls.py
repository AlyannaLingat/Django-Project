from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index1, name="index"),
]

urlpatterns = [
    path("Yanna", views.Yanna, name="Yanna"),
]
urlpatterns = [ 
    path("Sam", views.Sam, name="Sam"),
]

urlpatterns = [ 
    path("<str:name>", views.greet, name="greet")
]
