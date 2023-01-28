from cachetools import cached, TTLCache
import requests


class OpenExchangeClient:
    base_url = 'https://openexchangerates.org/api'

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self) -> dict:
        return requests.get(f'{self.base_url}/latest.json?app_id={self.app_id}').json()

    def convert(self, from_amount: int, from_currency: str, to_currency: str) -> int:
        conversion_rates = self.latest['rates']
        to_rate = conversion_rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate

        else:
            from_in_USD = from_amount / conversion_rates[from_currency]
            return from_in_USD * to_rate
