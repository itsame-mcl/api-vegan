from fastapi import FastAPI
import server.off as OFF

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/is_vegan/{item_id}")
def is_vegan(item_id: int):
    result = OFF.get_info(item_id)
    ingredients_analysis_tags = result['product']['ingredients_analysis_tags']
    if "en:vegan" in ingredients_analysis_tags:
        is_vegan = "yes"
    elif "en:non-vegan" in ingredients_analysis_tags:
        is_vegan = "no"
    elif "en:vegan-status-maybe" in ingredients_analysis_tags:
        is_vegan = "maybe"
    else:
        is_vegan = "unknown"
    return {item_id: is_vegan}