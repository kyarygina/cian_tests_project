import json
import logging
import os
import allure
from allure_commons._allure import step
from allure_commons.types import Severity, AttachmentType
from dotenv import load_dotenv
from jsonschema import validate

from schemas.get_agencies_response import get_agencies_response

load_dotenv()
BASE_API_URL = os.getenv("CIAN_API_URL")

@allure.epic("API Tests")
@allure.feature("Агенства")
@allure.story("Проверки для api раздела с агентствами")
class TestAgenciesApi:

    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    @allure.label("owner", "kyarygina")
    def test_success_get_agencies(self, auth_data):

        search_text = "INVEST7"

        with step("Выполнить запрос на получение агенства"):
            url = f"{BASE_API_URL}/agent-catalog-search/v1/get-agencies/"
            params = {
                "searchText": search_text,
                "regionId": 1,
                "page": 1,
                "limit": 10,
            }
            r = auth_data.get(url, params=params)

        # Логируем ответ в консоль
        logging.info(f"Response: status={r.status_code} url={r.url}")


        # Allure: Response
        allure.attach(json.dumps(r.json(), indent=4, ensure_ascii=False),
                      name="Response Body", attachment_type=AttachmentType.JSON)

        resp_json = r.json()

        with step("Проверить, что в ответе вернулся statusCode = 200"):
            assert r.status_code == 200

        with step("Проверить, что в ответе вернулось агентство, которое было запрошено"):
            assert resp_json["items"][0]["name"] == search_text

        with step("Проверить, что ответ соответстсвует json схеме"):
            validate(resp_json, get_agencies_response)