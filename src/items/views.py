from django.views import View
from django.views.generic import DetailView

from items.models import Item


class ItemView(DetailView):
    """Представление модели Item"""
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'


class BuyView(View):
    pass
