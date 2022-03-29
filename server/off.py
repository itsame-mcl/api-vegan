import requests


def search_code(product_name : str):
    payload = {"search_terms": product_name, "search_simple": 1, "action": "process", "json": 1}
    r = requests.get("https://world.openfoodfacts.org/cgi/search.pl", params=payload)
    if r.status_code == 200:
        return r.json()
    else:
        raise ConnectionError

def get_info(item_id : int):
    r = requests.get("https://world-fr.openfoodfacts.org/api/v0/product/" + str(item_id) + ".json")
    if r.status_code == 200:
        return r.json()
    else:
        raise ConnectionError
