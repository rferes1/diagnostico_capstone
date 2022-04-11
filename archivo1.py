
import requests
import time

skus_mover = {
    "108": 24,
    "122": 37,
    "113": 29,
    "117": 28,
    "129": 11
}

for key,value in skus_mover.items():
    URL = f"http://aysen18.ing.puc.cl/stocks/move-almacen?almacenOrigen=60ccc5559092f700042392df&almacenDestino=60ccc5559092f700042392e0&sku={key}&cantidad={value}"
    r = requests.post(url=URL)
    print(f"Status {r}  - sku {key} - cantidad {value}")
    time.sleep(20)