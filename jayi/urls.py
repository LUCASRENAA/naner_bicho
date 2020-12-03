"""jayi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit',views.submit_login),
                  path ( 'login/cadastrar', views.cadastrar_usuario ),
                  path ( 'login/voltar', views.voltar ),
                  path ( 'login/cadastrar/voltar', views.voltar ),
                  path ( 'login/cadastrar/submit', views.cadastrar_confirmar ),
                  path('inicio/online',views.online),

                  path('inicio/logout/',views.logout_user),
    path('inicio/',views.inicio),
    path('inicio/jogadas/', views.jogadas),
    path('inicio/jogar/', views.jogar),
    path('inicio/jogar/pule/', views.ver_pule),
    path('inicio/jogar/submit', views.jogar_valor),
    path('inicio/resultado/',views.resultado),
    path('inicio/girar/',views.girar),
    path('inicio/dinheiro/',views.dinheiro),
    path ('inicio/resultado/conferir/', views.conferir_resultado ),
    path('inicio/jogar/teste/', views.teste),
    path('inicio/testando2', views.teste_script),
    path('inicio/seudinheiro', views.dinheiro_rodada),
    path ('inicio/conteiner', views.conteiner ),
    path ('inicio/avaliacao', views.avaliacao ),
    path ( 'inicio/comojogar', views.comojogar ),
    path ( 'inicio/submit', views.submit_avaliacao ),
    path ( 'teste', views.imagem ),
    path ( '', RedirectView.as_view ( url = 'inicio/' ) )
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

