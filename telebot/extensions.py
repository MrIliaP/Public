import json
import requests
from config import keys

class ConversionException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(amount: str, quote: str, base: str):
        if quote == base:
            raise ConversionException(f"I dont like to convert similar currencies - {base}. "
                                      f"Try again.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'I dont work with - {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'I dont work with - {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Amount {amount} is wrong')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[keys[base]])

        return total_base