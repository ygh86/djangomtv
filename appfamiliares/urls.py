from django.urls import path
from . import views

app_name = "appfamiliares"

urlpatterns = [
    path('familiares/listado', views.lista_familiares, name='lista_familiares'),
    path('familiares/detalle/<int:id>/', views.detalle_familiar, name='detalle_familiar'),
]