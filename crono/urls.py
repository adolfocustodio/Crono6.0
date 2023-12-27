from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('categoria/', include('categorias.urls', namespace='categorias')),
    path('postagem/', include('postagens.urls', namespace='postagens')),
    path('admin/', admin.site.urls)
]
