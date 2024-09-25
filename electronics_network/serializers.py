from rest_framework import serializers

from electronics_network.models import Contact, Product, Factory


class ContactSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Контакты` для общего вида.
    """

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Продукты` для общего вида.
    """

    class Meta:
        model = Product
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    """
    Обработка модели `Завод` для общего вида.
    """

    class Meta:
        model = Factory
        fields = ('id', 'name', 'contacts', 'products')


class FactoryRetrieveSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Завод` для детального просмотра.
    """

    class Meta:
        model = Factory
        fields = ('id', 'name', 'contacts', 'products', 'supplier', 'dept', 'creation_time')
        depth = 1
