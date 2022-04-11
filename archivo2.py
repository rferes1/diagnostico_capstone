import requests
import time


formulas = {
    "10001": {"107": 6 ,"100": 6, "1000": 12,  "108": 6 ,  "114": 6 ,  "112": 6 ,  "119": 6 ,  "129": 12 ,  "113": 6 ,  "118": 6},
    "10002": {"1001": 8,  "121": 8,  "120": 16,  "115": 8,  "113": 16},
    "10003": {"1002":5, "121":5, "124":10, "125":5, "111":5, "128":5, "117":5, "129":5, "113":5, "116":10},
    "10004": {"1003":10, "104":10, "109":5, "117":5, "128":5, "113": 5, "122":10},
    "10005": {"1000": 12 ,  "126": 4 ,  "114": 4 ,  "100": 4 ,  "127": 4 ,  "132": 8 ,  "110": 4 ,  "103": 4 ,  "102": 4 ,  "129": 4},
    "10006": {"1003": 9, "113":9, "129":9, "111":9,"116":9, "128":9, "117":18}
    }

lotes = {
    "10001": 6, "10002": 8, "10005": 4 ,"10003":5 , "10004": 6, "10006": 9
}

def mover_productos_a_despacho(sku, formulas):
    formula = formulas[sku]
    for sku_2, cantidad in formula.items():
        url = f"http://aysen18.ing.puc.cl/stocks/move-almacen?almacenOrigen=60ccc5559092f700042392e0&almacenDestino=60ccc5559092f700042392df&sku={sku_2}&cantidad={cantidad}"

        #print(url)
        r = requests.post(url=url)
        print(f"Status {r}  - sku {sku_2} - cantidad {cantidad}")
        time.sleep(10)

def fabricar_vacunas_resagadas(sku, lotes):
    URL = "http://aysen18.ing.puc.cl/fabricar_vacuna_resagada"
    cantidad = lotes[sku]
    PARAMS = {"sku": sku, "cantidad": cantidad}
    r = requests.put(url=URL, params=PARAMS)
    print(f"Status {r}  - sku {sku} - cantidad {cantidad}")
    # print(PARAMS)
    time.sleep(8)
mover_productos_a_despacho("10004", formulas)
fabricar_vacunas_resagadas("10004", lotes)