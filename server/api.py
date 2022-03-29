from fastapi import FastAPI
import server.off as off

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_EAN/{product_name}")
def get_ean(product_name : str):
    res = off.search_code(product_name)
    if res['count'] > 0:
        return int(res['products'][0]['_id'])


@app.get("/is_vegan/{item_id}")
def is_vegan(item_id: int):
    result = off.get_info(item_id)
    ingredients_analysis_tags = result['product']['ingredients_analysis_tags']
    match ingredients_analysis_tags:
        case _ if "en:vegan" in ingredients_analysis_tags:
            vegan = "yes"
        case _ if "en:non-vegan" in ingredients_analysis_tags:
            vegan = "no"
        case _ if "en:vegan-status-maybe" in ingredients_analysis_tags:
            vegan = "maybe"
        case _:
            vegan = "unknown"
    return {item_id: vegan}
