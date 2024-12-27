from config.settings import STRIPE_API_KEY
import stripe

stripe.api_key = STRIPE_API_KEY


# def convert_rub_to_dollars(amount):
#     """ Перевод доллара в рубли """
#
#     c = CurrencyRates()
#     rate = c.get_rate('RUB', 'USD')
#     return int(amount * rate)


def create_stripe_price(amount):
    """ Создаем цену на сайте STRIPE """

    stripe.api_key = STRIPE_API_KEY

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 90,
        product_data={"name": "Course Subscription"},
    )


def create_stripe_session(price):
    """ Создает сессию на оплату в STRIPE. """

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/course/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )

    return session.get('id'), session.get('url')
