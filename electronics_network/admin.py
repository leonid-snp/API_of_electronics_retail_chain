from django.contrib import admin

from electronics_network.models import Entrepreneur, Factory, RetailChain


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """
    Класс `Завод` - отображения в админ-панели.
    """
    list_display = ('id', 'name', 'contacts', 'dept', 'creation_time')
    list_filter = ('contacts',)


@admin.register(RetailChain)
class RetailChainAdmin(admin.ModelAdmin):
    """
    Класс `Розничная сеть` - отображение в админ-панели.
    """
    list_display = ('id', 'name', 'contacts', 'dept', 'creation_time')
    list_filter = ('contacts',)


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    """
    Модель `Предприниматель` - отображение в админ-панели.
    """
    list_display = ('id', 'name', 'contacts', 'dept', 'creation_time')
    list_filter = ('contacts',)
