"""
URL configuration for Patinhas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from aplic.views import IndexView
from django.conf.urls.static import static
from django.conf import settings
from aplic.views import cadastrar_usuario

router = SimpleRouter()

urlpatterns = [
    path('cadastro/', cadastrar_usuario, name="cadastrar_usuario"),
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
