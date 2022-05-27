from django.contrib import admin
from django.urls import path

from familiares.views import mostrar_familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/',mostrar_familia, name = 'familia'),
]