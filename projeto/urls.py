

from django.contrib.auth.views import logout_then_login
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
# carregando arquivos estaticos no deploy: https://tutorial.djangogirls.org/pt/deploy/


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('projeto.core.urls')),
    path('logout/', logout_then_login, name='logout'),
    path('user/', include('projeto.accounts.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
