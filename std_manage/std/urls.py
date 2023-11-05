from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("home/",home),
    path("add-std/",std_add),
    path("delete-std/<int:roll>",std_delete),
    path("update-std/<int:roll>",std_update),
    path("do-update-std/<int:roll>",do_std_update),
]
