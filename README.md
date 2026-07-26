# Inventory Management System

A Flask-based REST API for managing inventory items. This project supports full CRUD operations, integrates with the OpenFoodFacts API, and includes a CLI application for interacting with the API.

---

## Features

- View all inventory items
- View a single inventory item
- Add new inventory items
- Update existing inventory items
- Delete inventory items
- Search inventory by brand
- Fetch product information from OpenFoodFacts
- Import products from OpenFoodFacts into the inventory
- Command Line Interface (CLI)
- Unit tests using pytest

---

## Technologies Used

- Python 3
- Flask
- Requests
- Pytest
- Pipenv

---

## Installation

Clone the repository

```bash
git clone https://github.com/penzimbuthia-sudo/inventory-management
cd inventory-management
```

Install dependencies

```bash
pipenv install
```

Activate the virtual environment

```bash
pipenv shell
```

---

## Running the Flask API

```bash
python app.py
```

The server starts at

```
http://127.0.0.1:5000
```

## Running the CLI

Open another terminal and run

```bash
python cli.py
```


## Running Tests

```bash
pytest
```

## API Endpoints

### Home

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Welcome message |

### Inventory

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /inventory | Get all inventory items |
| GET | /inventory/<id> | Get one inventory item |
| POST | /inventory | Create a new inventory item |
| PATCH | /inventory/<id> | Update an inventory item |
| DELETE | /inventory/<id> | Delete an inventory item |

### Helper Routes

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /inventory/search/<brand> | Search inventory by brand |

### OpenFoodFacts

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /product/<barcode> | Fetch product details |
| POST | /import/<barcode> | Import product into inventory |


## Example Requests

### Create Item

POST /inventory

```json
{
    "product_name": "Milk",
    "brand": "Brookside",
    "price": 120,
    "stock": 10
}
```

Response

```json
{
    "id": 2,
    "product_name": "Milk",
    "brand": "Brookside",
    "price": 120,
    "stock": 10
}
```


### Update Item

PATCH /inventory/2

```json
{
    "price": 150
}
```

### Delete Item

DELETE /inventory/2

### Search by Brand

GET

```
/inventory/search/Silk
```

### Fetch Product

GET

```
/product/737628064502
```


### Import Product

POST

```
/import/737628064502
```

## Project Structure

```
inventory-management/
│
├── app.py
├── cli.py
├── test_app.py
├── Pipfile
├── Pipfile.lock
└── README.md
```


## Testing

The project includes automated tests for:

- Home route
- CRUD operations
- Validation errors
- Search route
- External API integration
- Product import functionality

Run

```bash
pytest
```

## Author

Penzi Mbuthia