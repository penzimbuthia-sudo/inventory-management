from app import app
from unittest.mock import patch

def test_get_inventory():

    client = app.test_client()

    response = client.get("/inventory")

    assert response.status_code == 200

def test_get_single_item():

    client = app.test_client()

    response = client.get("/inventory/1")

    assert response.status_code == 200

def test_create_item():

    client = app.test_client()

    response = client.post(
        "/inventory",
        json={
            "product_name": "Milk",
            "brand": "Brookside",
            "price": 120,
            "stock": 10
        }
    )

    assert response.status_code == 201

def test_update_item():

    client = app.test_client()

    response = client.patch(
        "/inventory/1",
        json={
            "price": 999
        }
    )

    assert response.status_code == 200

def test_delete_item():

    client = app.test_client()

    response = client.delete(
        "/inventory/1"
    )

    assert response.status_code == 200

@patch("requests.get")
def test_external_api(mock_get):

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk"
        }
    }

    response = mock_get.return_value.json()

    assert response["status"] == 1