from django.urls import path

from electronics_network.apps import ElectronicsNetworkConfig
from electronics_network.views import (ContactCreateAPIView,
                                       ProductCreateAPIView, FactoryCreateAPIView, FactoryRetrieveAPIView,
                                       FactoryUpdateAPIView, FactoryDestroyAPIView, FactoryListAPIView)

app_name = ElectronicsNetworkConfig.name

urlpatterns = [
    path('contact/create/', ContactCreateAPIView.as_view(), name='contact-create'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),

    path('factory/create/', FactoryCreateAPIView.as_view(), name='factory-create'),
    path('factory/<int:pk>/retrieve/', FactoryRetrieveAPIView.as_view(), name='factory-retrieve'),
    path('factory/<int:pk>/update/', FactoryUpdateAPIView.as_view(), name='factory-update'),
    path('factory/<int:pk>/destroy/', FactoryDestroyAPIView.as_view(), name='factory-destroy'),
    path('factory/list/', FactoryListAPIView.as_view(), name='factory-list')
]
