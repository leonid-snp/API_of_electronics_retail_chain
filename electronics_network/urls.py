from django.urls import path

from electronics_network.apps import ElectronicsNetworkConfig
from electronics_network.views import (ContactCreateAPIView,
                                       ProductCreateAPIView, FactoryCreateAPIView, FactoryRetrieveAPIView,
                                       FactoryUpdateAPIView, FactoryDestroyAPIView, FactoryListAPIView,
                                       RetailChainCreateAPIView, RetailChainRetrieveAPIView, RetailChainUpdateAPIView)

app_name = ElectronicsNetworkConfig.name

urlpatterns = [
    path('contact/create/', ContactCreateAPIView.as_view(), name='contact-create'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),

    path('factory/create/', FactoryCreateAPIView.as_view(), name='factory-create'),
    path('factory/<int:pk>/retrieve/', FactoryRetrieveAPIView.as_view(), name='factory-retrieve'),
    path('factory/<int:pk>/update/', FactoryUpdateAPIView.as_view(), name='factory-update'),
    path('factory/<int:pk>/destroy/', FactoryDestroyAPIView.as_view(), name='factory-destroy'),
    path('factory/list/', FactoryListAPIView.as_view(), name='factory-list'),

    path('retail-chain/create/', RetailChainCreateAPIView.as_view(), name='retail-chain-create'),
    path('retail-chain/<int:pk>/retrieve/', RetailChainRetrieveAPIView.as_view(), name='retail-chain-retrieve'),
    path('retail-chain/<int:pk>/update/', RetailChainUpdateAPIView.as_view(), name='retail-chain-update')
]
