from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from electronics_network.models import Contact, Product, Factory
from electronics_network.serializers import (ContactSerializer,
                                             ProductSerializer, FactorySerializer, FactoryRetrieveSerializer)


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
    serializer_class = FactorySerializer


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
