from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from electronics_network.models import Entrepreneur, Factory, RetailChain


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """
    Класс `Завод` - отображения в админ-панели.
    """
    list_display = ('name', 'contacts', 'dept', 'creation_time')
    list_filter = ('contacts__city', 'contacts__country')
    list_display_links = ('name',)


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    """
    Модель `Предприниматель` - отображение в админ-панели.
    """
    list_display = ('name', 'contacts', 'display_venue', 'dept', 'creation_time')
    list_filter = ('contacts__city', 'contacts__country',)
    list_display_links = ('name',)
    actions = ('dept_zero',)
    list_select_related = ('supplier',)

    @admin.action(description='Снять задолженность')
    def dept_zero(self, request, queryset):
        count = queryset.update(dept=0)
        self.message_user(request, f'Обнулено {count} записей.')

    def display_venue(self, obj):
        link = reverse("admin:electronics_network_factory_change", args=[obj.supplier.id])
        return format_html('<a href="{}">{}</a>', link, obj.supplier)

    display_venue.short_description = "Поставщик"


@admin.register(RetailChain)
class RetailChainAdmin(admin.ModelAdmin):
    """
    Класс `Розничная сеть` - отображение в админ-панели.
    """
    list_display = ('name', 'contacts', 'display_venue', 'dept', 'creation_time')
    list_filter = ('contacts__city', 'contacts__country',)
    list_display_links = ('name',)
    actions = ('dept_zero',)
    list_select_related = ('supplier',)

    @admin.action(description='Снять задолженность')
    def dept_zero(self, request, queryset):
        count = queryset.update(dept=0)
        self.message_user(request, f'Обнулено {count} записей.')

    def display_venue(self, obj):
        link = reverse("admin:electronics_network_entrepreneur_change", args=[obj.supplier.id])
        return format_html('<a href="{}">{}</a>', link, obj.supplier)

    display_venue.short_description = "Поставщик"
