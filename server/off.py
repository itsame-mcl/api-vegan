import requests


def get_info(item_id : int):
    r = requests.get("https://world-fr.openfoodfacts.org/api/v0/product/" + str(item_id))
    if r.status_code == 200:
        return r.json()
    else:
        raise ConnectionError
