import time

from libs.openexchange import OpenExchangeClient

APP_ID = "0b73ed75de934f7d9aa0c85e2251408f"

client = OpenExchangeClient(APP_ID)

USD_amount = 1000
start = time.time()
GBP_amount = client.convert(USD_amount, "USD", "GBP")
end = time.time()

print(end - start)

print(f'\nIf you have {USD_amount} dollars...')
print(f'The exchange for {USD_amount} dollars is {GBP_amount} British pounds!\n')