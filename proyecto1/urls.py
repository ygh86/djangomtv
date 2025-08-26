"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#importo las vistas
from appfamiliares import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Main.urls")),  # Ruta para la vista index de appfamiliares
    path('familiares/', include("appfamiliares.urls")),  # Ruta para la lista de familiares
    #path('detalle_familiar/<int:id>/', include("appfamiliares.urls")),  # Ruta para el detalle de un familiar
]
