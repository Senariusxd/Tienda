
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from Objeto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('generos', views.lista_generos, name='lista_generos'),
    path('crear/', views.crear_generos, name='crear_generos'),
    path('editar/<int:pk>/', views.editar_generos, name='editar_genero'),
    path('eliminar/<int:pk>/', views.eliminar_generos, name='eliminar_genero'),
    
    path('genero/<int:genero_id>/productos/', views.lista_productos, name='lista_productos'),
    path('genero/<int:genero_id>/productos/crear/', views.crear_productos , name='crear_productos'),
    path('genero/<int:genero_id>/productos/editar/<int:pk>/', views.editar_productos, name='editar_productos'),
    path('genero/<int:genero_id>/productos/eliminar/<int:pk>/', views.eliminar_productos, name='eliminar_productos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
