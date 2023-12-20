from django.http import HttpRequest, JsonResponse
from django.urls import reverse

from django.views import View
from django.views.generic import DetailView

from items.models import Item
from items.services import get_stripe_checkout_session


class ItemView(DetailView):
    """Представление модели Item"""
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'


class BuyView(View):
    """Возвращает Stripe Session id для оплаты выбранного Item"""
    def get(self, request: HttpRequest, id: int):
        success_url = request.build_absolute_uri(reverse(
            viewname='item-view',
            args=[id,]
        ))
        session = get_stripe_checkout_session(
            item_id=id,
            success_url=success_url
        )
        return JsonResponse({"session_id": session.id})
