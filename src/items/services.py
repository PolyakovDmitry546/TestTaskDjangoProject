from django.shortcuts import get_object_or_404

import stripe
from stripe.checkout import Session

from config.settings import STRIPE_SECRET_KEY
from items.models import Item


def get_stripe_checkout_session(item_id: int, success_url: str) -> Session:
    """Возвращает Stripe Session для оплаты товара item_id

    Args:
        item_id (int): id товара
        success_url (str): url для перенаправления после успешной оплаты
    """
    item = get_object_or_404(Item, id=item_id)

    # Список товаров для оплаты
    line_items = [
        {
            'price_data': {
                'currency': 'USD',
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': item.price,
            },
            'quantity': 1
        },
    ]
    session = stripe.checkout.Session.create(
        api_key=STRIPE_SECRET_KEY,
        success_url=success_url,
        line_items=line_items,
        mode='payment'
    )
    return session
