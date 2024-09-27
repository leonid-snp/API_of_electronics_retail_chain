from rest_framework import serializers

from electronics_network.models import Contact, Product, Factory, RetailChain, Entrepreneur


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


class FactoryUpdateSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Завод` для редактирования.
    """

    class Meta:
        model = Factory
        fields = ('id', 'name', 'contacts', 'products', 'supplier')


class EntrepreneurSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Предприниматель` для общего вида.
    """

    class Meta:
        model = Entrepreneur
        fields = ('id', 'name', 'contacts', 'products')


class EntrepreneurRetrieveSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Предприниматель` для детального просмотра.
    """

    class Meta:
        model = Entrepreneur
        fields = ('id', 'name', 'contacts', 'products', 'supplier', 'dept', 'creation_time')
        depth = 1


class EntrepreneurUpdateSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Предприниматель` для редактирования.
    """

    class Meta:
        model = Entrepreneur
        fields = ('id', 'name', 'contacts', 'products', 'supplier')


class RetailChainSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Розничная сеть` для общего просмотра.
    """

    class Meta:
        model = RetailChain
        fields = ('id', 'name', 'contacts', 'products')


class RetailChainRetrieveSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Розничная сеть` для детального просмотра.
    """

    class Meta:
        model = RetailChain
        fields = ('id', 'name', 'contacts', 'products', 'supplier', 'dept', 'creation_time')
        depth = 1


class RetailChainUpdateSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Розничная сеть` для редактирования
    """

    class Meta:
        model = RetailChain
        fields = ('id', 'name', 'contacts', 'products', 'supplier')
