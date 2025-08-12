

def create_folder(session, cian_cookie, name: str) -> int:
    url = "https://api.cian.ru/favorites/v1/web/create-folder/"
    payload = {"name": name}
    cookies = {"_CIAN_GK": cian_cookie}
    r = session.post(url, json=payload, cookies=cookies)
    r.raise_for_status()
    data = r.json()
    if data.get("status") != "ok":
        raise RuntimeError(f"Ошибка создания папки: {data}")
    folder_id = data.get("folderId")
    if not folder_id:
        raise RuntimeError("Не получили folderId после создания папки")
    return folder_id