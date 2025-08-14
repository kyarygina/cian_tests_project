import json
import logging
import os
import allure
import pytest
from allure_commons._allure import step
from allure_commons.types import AttachmentType, Severity
from dotenv import load_dotenv
from jsonschema import validate
from api.add_favorite_api import get_newbuilding_data, add_newbuilding_to_favorite
from models.category_mapping import CATEGORY_TO_ENTITYTYPE
from schemas.add_favorite_request import add_favorite_request
from schemas.add_favorite_response import add_favorite_response
from schemas.delete_favorite_request import delete_favorite_request
from schemas.delete_favorite_response import delete_favorite_response

load_dotenv()
BASE_API_URL = os.getenv("CIAN_API_URL")

@allure.epic("API Tests")
@allure.feature("Избранные объявления")
@allure.story("Проверки для api избранных объявлений")
class TestFavoritesAdsApi:

    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    @allure.label("owner", "kyarygina")
    def test_success_add_ad_favorites(self, auth_data):

        newbuilding_id, deal_type, category = get_newbuilding_data(auth_data)

        entity_type = CATEGORY_TO_ENTITYTYPE.get(category)

        fav_payload = {
            "entityId": newbuilding_id,
            "dealType": deal_type,
            "entityType": entity_type,
            "addToFolder": True
        }

        # Логируем запрос в консоль
        logging.info(f"POST /favorites/v1/add-favorite payload={fav_payload}")

        with step("Провалидировать схему запроса"):
            validate(fav_payload, add_favorite_request)


        with step("Выполнить запрос на добавление объявления в избранное"):
            fav_url = f"{BASE_API_URL}/favorites/v1/add-favorite/"
            r = auth_data.post(fav_url, json=fav_payload)

        # Логируем ответ в консоль
        logging.info(f"Response: status={r.status_code} url={r.url}")

        # Allure: Request
        allure.attach(json.dumps(fav_payload, indent=4, ensure_ascii=False),
                      name="Request Payload", attachment_type=AttachmentType.JSON)
        # Allure: Response
        allure.attach(json.dumps(r.json(), indent=4, ensure_ascii=False),
                      name="Response Body", attachment_type=AttachmentType.JSON)

        resp_json = r.json()

        with step("Проверить, что в ответе вернулся statusCode = 200"):
            assert r.status_code == 200

        with step("Проверить, что объявление добавлено в избранное"):
            assert "isAdded" in resp_json, "В ответе нет признака isAdded"
            assert resp_json["isAdded"] is True

        with step("Проверить, что ответ соответстсвует json схеме"):
            validate(resp_json, add_favorite_response)

    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    @allure.label("owner", "kyarygina")

    def test_unsuccess_add_ad_favorites(self, auth_data):

        newbuilding_id, deal_type, category = get_newbuilding_data(auth_data)

        entity_type = CATEGORY_TO_ENTITYTYPE.get(category)
        if not entity_type:
            raise RuntimeError(f"Неизвестная категория {category}")

        fav_payload = {
            "entityId": None,
            "dealType": deal_type,
            "entityType": entity_type,
            "addToFolder": True
        }

        # Логируем запрос в консоль
        logging.info(f"POST /favorites/v1/add-favorite payload={fav_payload}")

        with step("Провалидировать схему запроса"):
            validate(fav_payload, add_favorite_request)

        with step("Выполнить запрос на добавление объявления в избранное"):
            fav_url = f"{BASE_API_URL}/favorites/v1/add-favorite/"
            r = auth_data.post(fav_url, json=fav_payload)

        # Логируем ответ в консоль
        logging.info(f"Response: status={r.status_code} url={r.url}")

        # Allure: Request
        allure.attach(json.dumps(fav_payload, indent=4, ensure_ascii=False),
                      name="Request Payload", attachment_type=AttachmentType.JSON)
        # Allure: Response
        allure.attach(json.dumps(r.json(), indent=4, ensure_ascii=False),
                      name="Response Body", attachment_type=AttachmentType.JSON)


        with step("Проверить, что в ответе вернулся statusCode = 400"):
            assert r.status_code == 400


    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    @allure.label("owner", "kyarygina")
    @pytest.mark.parametrize("offer_index", [1, 2])
    def test_success_delete_ad_favorites(self, auth_data, offer_index):

        newbuilding_id, entity_type = add_newbuilding_to_favorite(auth_data, offer_index=offer_index)

        fav_payload = {
            "entities": [
                {
                    "entityIds": [
                        newbuilding_id
                    ],
                    "entityType": entity_type
                }
            ]
        }

        # Логируем запрос в консоль
        logging.info(f"POST /favorites/v1/web/delete-favorite-by-ids/ payload={fav_payload}")

        with step("Провалидировать схему запроса"):
            validate(fav_payload, delete_favorite_request)

        with step("Выполнить запрос на удаление объявления из избранного"):
            fav_url = f"{BASE_API_URL}/favorites/v1/web/delete-favorite-by-ids/"
            r = auth_data.post(fav_url, json=fav_payload)

        # Логируем ответ в консоль
        logging.info(f"Response: status={r.status_code} url={r.url}")

        # Allure: Request
        allure.attach(json.dumps(fav_payload, indent=4, ensure_ascii=False),
                      name="Request Payload", attachment_type=AttachmentType.JSON)
        # Allure: Response
        allure.attach(json.dumps(r.json(), indent=4, ensure_ascii=False),
                      name="Response Body", attachment_type=AttachmentType.JSON)

        resp_json = r.json()

        with step("Проверить, что в ответе вернулся statusCode = 200"):
            assert r.status_code == 200

        with step("Проверить, что ответ соответстсвует json схеме"):
            validate(resp_json, delete_favorite_response)

    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    @allure.label("owner", "kyarygina")
    @pytest.mark.parametrize("offer_index", [1, 2])
    def test_unsuccess_delete_ad_favorites(self, auth_data, offer_index):
        newbuilding_id, entity_type = add_newbuilding_to_favorite(auth_data, offer_index=offer_index)

        fav_payload = {
            "entities": [
                {
                    "entityIds": [
                        newbuilding_id
                    ],
                    "entityType": "fail_type"
                }
            ]
        }

        # Логируем запрос в консоль
        logging.info(f"POST /favorites/v1/web/delete-favorite-by-ids/ payload={fav_payload}")

        with step("Провалидировать схему запроса"):
            validate(fav_payload, delete_favorite_request)

        with step("Выполнить запрос на удаление объявления из избранного"):
            fav_url = f"{BASE_API_URL}/favorites/v1/web/delete-favorite-by-ids/"
            r = auth_data.post(fav_url, json=fav_payload)

        # Логируем ответ в консоль
        logging.info(f"Response: status={r.status_code} url={r.url}")

        # Allure: Request
        allure.attach(json.dumps(fav_payload, indent=4, ensure_ascii=False),
                      name="Request Payload", attachment_type=AttachmentType.JSON)
        # Allure: Response
        allure.attach(json.dumps(r.json(), indent=4, ensure_ascii=False),
                      name="Response Body", attachment_type=AttachmentType.JSON)

        resp_json = r.json()

        with step("Проверить, что в ответе вернулся statusCode = 400"):
            assert r.status_code == 400

        with step("Проверить, что ответ соответстсвует json схеме"):
            assert resp_json["message"] == "validation error"