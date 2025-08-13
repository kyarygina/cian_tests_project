import os

import requests
from allure_commons._allure import step
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = os.getenv("CIAN_API_URL")
BASE_WWW_URL = os.getenv("CIAN_WWW_URL")
LOGIN = os.getenv("CIAN_LOGIN")
PASSWORD = os.getenv("CIAN_PASSWORD")

def get_auth_cookie(login: str = LOGIN, password: str = PASSWORD):

    session = requests.Session()

    with step("Получить токен из ответа метода /v1/validate-login-password"):
        auth_url = f"{BASE_API_URL}/authentication/v1/validate-login-password/"
        auth_payload = {"login": login, "password": password}
        r = session.post(auth_url, json=auth_payload)
        r.raise_for_status()
        data = r.json()

        token = data["logOnInfo"][0]["token"]
        login_resp = data["login"]

        if not token:
            raise RuntimeError("Token не найден в ответе метода /v1/validate-login-password")
        if login_resp != login:
            raise RuntimeError(f"Логин в ответе '{login_resp}' != '{login}'")

    with step("Получить cookie из ответа метода /logon"):
        logon_url = f"{BASE_WWW_URL}/api/users/logon"
        r = session.get(logon_url, params={"login": login_resp, "token": token})
        r.raise_for_status()

        cian_cookie = session.cookies.get("_CIAN_GK")
        if not cian_cookie:
            raise RuntimeError("Сookie _CIAN_GK не найдена в ответе метода logon")

        return session, cian_cookie