from unittest.mock import patch

import pytest

from app import app, inventory


@pytest.fixture
def client():

    inventory.clear()

    inventory.append({
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 450,
        "stock": 20
    })

    return app.test_client()

def test_home(client):

    response = client.get("/")

    assert response.status_code == 200

def test_get_inventory(client):

    response = client.get("/inventory")

    assert response.status_code == 200

def test_get_single_item(client):

    response = client.get("/inventory/1")

    assert response.status_code == 200

def test_get_item_not_found(client):

    response = client.get("/inventory/999")

    assert response.status_code == 404

def test_create_item(client):

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

def test_create_item_missing_fields(client):

    response = client.post(
        "/inventory",
        json={}
    )

    assert response.status_code == 400

def test_update_item(client):

    response = client.patch(
        "/inventory/1",
        json={
            "price": 999
        }
    )

    assert response.status_code == 200

def test_update_item_not_found(client):

    response = client.patch(
        "/inventory/999",
        json={
            "price": 100
        }
    )

    assert response.status_code == 404

def test_delete_item(client):

    response = client.delete(
        "/inventory/1"
    )

    assert response.status_code == 200

def test_delete_item_not_found(client):

    response = client.delete(
        "/inventory/999"
    )

    assert response.status_code == 404

def test_search_inventory(client):
    
    response = client.get(
        "/inventory/search/Silk"
    )

    assert response.status_code == 200

def test_search_inventory_not_found(client):

    response = client.get(
        "/inventory/search/UnknownBrand"
    )

    assert response.status_code == 404

@patch("app.requests.get")
def test_get_product(mock_get, client):

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk"
        }
    }

    mock_get.return_value.raise_for_status.return_value = None

    response = client.get("/product/123456")

    assert response.status_code == 200  

@patch("app.requests.get")
def test_import_product(mock_get, client):

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk",
            "brands": "Silk"
        }
    }

    mock_get.return_value.raise_for_status.return_value = None

    response = client.post("/import/123456")

    assert response.status_code == 201    