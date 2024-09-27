from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('electronics-network/', include('electronics_network.urls', namespace='electronics-network'))
]

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Сеть продажи электроники'
