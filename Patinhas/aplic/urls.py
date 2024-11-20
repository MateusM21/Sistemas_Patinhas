from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import IndexView, CadastrarUsuario
from django.contrib.auth import views as auth_views


router = SimpleRouter()

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastro/', CadastrarUsuario.as_view(), name="cadastrar_usuario"),
    path('', IndexView.as_view(), name='index'),
]
