from allure_commons._allure import step

from api.authentication_api import get_auth_cookie

BASE_API_URL = "https://api.cian.ru"

def test_add_ad_favorites():
    session, cian_cookie = get_auth_cookie()

    with step("Выполнить запрос на добавление объявления в избранное"):
        fav_url = f"{BASE_API_URL}/favorites/v1/add-favorite/"
        fav_payload = {
            "entityId": 291360130,
            "dealType": "sale",
            "entityType": "offerResidental",
            "addToFolder": True
        }
        cookies = {"_CIAN_GK": cian_cookie}
        r = session.post(fav_url, json=fav_payload, cookies=cookies)
        r.raise_for_status()
        resp_json = r.json()

    with step("Проверить, что в ответе вернулся признак добавления товара в избранное"):
        assert resp_json.get("isAdded") == True, f"Ошибка добавления: {resp_json}"

def test_add_ad_favorites():
    session, cian_cookie = get_auth_cookie()

    with step("Выполнить запрос на добавление объявления в избранное"):
        fav_url = f"{BASE_API_URL}/favorites/v1/web/get-user-favorites/"
        fav_payload = {
            "entityId": 291360130,
            "dealType": "sale",
            "entityType": "offerResidental",
            "addToFolder": True
        }
        cookies = {"_CIAN_GK": cian_cookie}
        r = session.post(fav_url, json=fav_payload, cookies=cookies)
        r.raise_for_status()
        resp_json = r.json()

    with step("Проверить, что в ответе вернулся признак добавления товара в избранное"):
        assert resp_json.get("isAdded") == True, f"Ошибка добавления: {resp_json}"