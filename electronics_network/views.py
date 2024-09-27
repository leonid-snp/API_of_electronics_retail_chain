from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from electronics_network.models import Contact, Product, Factory, RetailChain, Entrepreneur
from electronics_network.serializers import (ContactSerializer,
                                             ProductSerializer, FactorySerializer, FactoryRetrieveSerializer,
                                             RetailChainSerializer, RetailChainRetrieveSerializer,
                                             FactoryUpdateSerializer, RetailChainUpdateSerializer,
                                             EntrepreneurSerializer, EntrepreneurRetrieveSerializer,
                                             EntrepreneurUpdateSerializer)


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


class EntrepreneurCreateAPIView(CreateAPIView):
    """
    Класс представления создания предпринимателя.
    """
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurRetrieveAPIView(RetrieveAPIView):
    """
    Класс представления детального просмотра предпринимателя.
    """
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurRetrieveSerializer


class EntrepreneurUpdateAPIView(UpdateAPIView):
    """
    Класс представления редактирования предпринимателя.
    """
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurUpdateSerializer


class EntrepreneurDestroyAPIView(DestroyAPIView):
    """
    Класс представления удаления предпринимателя.
    """
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


class EntrepreneurListAPIView(ListAPIView):
    """
    Класс представления вывода списка предпринимателей.
    """
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


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


class RetailChainDestroyAPIView(DestroyAPIView):
    """
    Класс представления удаления розничной сети.
    """
    queryset = RetailChain.objects.all()
    serializer_class = RetailChainSerializer


class RetailChainListAPIView(ListAPIView):
    """
    Класс представления вывода списка розничных сетей.
    """
    queryset = RetailChain.objects.all()
    serializer_class = RetailChainSerializer
