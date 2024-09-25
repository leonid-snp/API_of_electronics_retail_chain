from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from electronics_network.models import Contact, Product, Factory, RetailChain
from electronics_network.serializers import (ContactSerializer,
                                             ProductSerializer, FactorySerializer, FactoryRetrieveSerializer,
                                             RetailChainSerializer, RetailChainRetrieveSerializer,
                                             FactoryUpdateSerializer, RetailChainUpdateSerializer)


class ContactCreateAPIView(CreateAPIView):
    """
    Класс представления создания контакта.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductCreateAPIView(CreateAPIView):
    """
    Класс представления создания продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FactoryCreateAPIView(CreateAPIView):
    """
    Класс представления создания завода.
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryRetrieveAPIView(RetrieveAPIView):
    """
    Класс представления просмотра завода.
    """
    queryset = Factory.objects.all()
    serializer_class = FactoryRetrieveSerializer


class FactoryUpdateAPIView(UpdateAPIView):
    """
    Класс представления редактирования завода.
    """
    queryset = Factory.objects.all()
    serializer_class = FactoryUpdateSerializer


class FactoryDestroyAPIView(DestroyAPIView):
    """
    Класс представления удаления завода.
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryListAPIView(ListAPIView):
    """
    Класс представления просмотра списка заводов.
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class RetailChainCreateAPIView(CreateAPIView):
    """
    Класс представления создания розничной сети.
    """
    queryset = RetailChain.objects.all()
    serializer_class = RetailChainSerializer


class RetailChainRetrieveAPIView(RetrieveAPIView):
    """
    Класс представления просмотра розничной сети.
    """
    queryset = RetailChain.objects.all()
    serializer_class = RetailChainRetrieveSerializer


class RetailChainUpdateAPIView(UpdateAPIView):
    """
    Класс представления редактирования розничной сети.
    """
    queryset = RetailChain.objects.all()
    serializer_class = RetailChainUpdateSerializer
