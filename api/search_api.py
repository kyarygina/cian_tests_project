from allure_commons._allure import step

BASE_API = "https://api.cian.ru"


def get_first_newbuilding_data(session, cian_cookie):

    with step("Выполнить запрос на поиск объявлений"):
        url = f"{BASE_API}/search-engine/v1/search-offers-mobile-site/"
        payload = {
            "jsonQuery": {
                "_type": "flatsale",
                "sort": {"type": "term", "value": "price_object_order"},
                "engine_version": {"type": "term", "value": 2},
                "region": {"type": "terms", "value": [1, 4593]},
                "room": {"type": "terms", "value": [4]},
                "building_status": {"type": "term", "value": 2}
            },
            "subdomain": "www"
        }
        cookies = {"_CIAN_GK": cian_cookie}
        r = session.post(url, json=payload, cookies=cookies)
        r.raise_for_status()
        data = r.json()

        offers = data.get("offers")
        if not offers or not isinstance(offers, list):
            raise RuntimeError("В ответе нет списка offers")

    with step("Получить данные по первому обявлению в списке офферов"):
        first_offer = offers[0]
        newbuilding_id = first_offer.get("newbuildingId")
        deal_type = first_offer.get("dealType")
        category = first_offer.get("category")


    return newbuilding_id, deal_type, category