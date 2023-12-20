from django.urls import path

from items.views import BuyView, ItemView


urlpatterns = [
    path('item/<int:pk>', ItemView.as_view(), name='item-view'),
    path('buy/<int:id>', BuyView.as_view(), name='buy-view'),
]
