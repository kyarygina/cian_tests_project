from allure_commons._allure import step
from jsonschema import validate
from api.search_api import get_first_newbuilding_data
from schemas.add_favorite_response import add_favorite_response

BASE_API_URL = "https://api.cian.ru"

CATEGORY_TO_ENTITYTYPE = {
    "newBuildingFlatSale": "newbuilding",
    "flatShareSale": "offerResidental",
    "houseSale": "offerSuburban",
    "officeSale": "offerCommercial"
}

def test_add_ad_favorites(auth_data):

    session, cian_cookie = auth_data

    newbuilding_id, deal_type, category = get_first_newbuilding_data(session, cian_cookie)

    entity_type = CATEGORY_TO_ENTITYTYPE.get(category)
    if not entity_type:
        raise RuntimeError(f"Неизвестная категория {category}")

    with step("Выполнить запрос на добавление объявления в избранное"):
        fav_url = f"{BASE_API_URL}/favorites/v1/add-favorite/"
        fav_payload = {
            "entityId": newbuilding_id,
            "dealType": deal_type,
            "entityType": entity_type,
            "addToFolder": True
        }
        cookies = {"_CIAN_GK": cian_cookie}
        r = session.post(fav_url, json=fav_payload, cookies=cookies)
        r.raise_for_status()
        resp_json = r.json()

    with step("Проверить, что в ответе вернулся statusCode = 200"):
        assert r.status_code == 200

    with step("Проверить, что в ответе вернулся признак добавления товара в избранное"):
        assert resp_json.get("isAdded") == True

    with step("Проверить, что ответ соответстсвует json схеме"):
        validate(resp_json, add_favorite_response)