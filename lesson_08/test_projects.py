import requests

from config import BASE_URL, TOKEN

MYHEADER = {
    "Authorization": f"Bearer {TOKEN}"
}


def test_create_project():
    resp = requests.post(
        BASE_URL + "api-v2/projects",
        headers=MYHEADER,
        json={"title": "Проект для создания"}
    )
    body = resp.json()
    projects_id = body["id"]

    assert resp.status_code == 201
    assert len(body) > 0
    requests.put(
            BASE_URL + "api-v2/projects/" + projects_id,
            headers=MYHEADER,
            json={"deleted": True}
        )


def test_get_project_by_id():
    resp = requests.post(
        BASE_URL + "api-v2/projects",
        headers=MYHEADER,
        json={"title": "Проект для получения"}
    )
    body = resp.json()
    projects_id = body["id"]
    resp_get = requests.get(
        BASE_URL + "api-v2/projects/" + projects_id,
        headers=MYHEADER
    )

    assert resp_get.status_code == 200
    requests.put(
            BASE_URL + "api-v2/projects/" + projects_id,
            headers=MYHEADER,
            json={"deleted": True}
        )


def test_update_project_by_id():
    resp = requests.post(
        BASE_URL + "api-v2/projects",
        headers=MYHEADER,
        json={"title": "Проект для обновления"}
    )
    body = resp.json()
    projects_id = body["id"]
    resp_put = requests.put(
        BASE_URL + "api-v2/projects/" + projects_id,
        headers=MYHEADER,
        json={"title": "Обновленное название проекта"}
    )

    assert resp_put.status_code == 200

    requests.put(
        BASE_URL + "api-v2/projects/" + projects_id,
        headers=MYHEADER,
        json={"deleted": True}
    )


def test_get_project_with_invalid_id():
    resp = requests.get(
        BASE_URL + "api-v2/projects/no-such-id-12345",
        headers=MYHEADER
    )

    assert resp.status_code in (404,)


def test_create_project_without_token():
    resp = requests.post(
        BASE_URL + "api-v2/projects",
        json={"title": "Проект без токена"}
    )

    assert resp.status_code in (401,)


def test_create_project_with_empty_title():
    resp = requests.post(
        BASE_URL + "api-v2/projects",
        headers=MYHEADER,
        json={"title": ""}
    )

    assert resp.status_code in (400,)
