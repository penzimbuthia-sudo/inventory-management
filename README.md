# Inventory Management System

## Overview

This project is a Flask-based REST API for managing inventory items. It supports CRUD operations, OpenFoodFacts API integration, a command-line interface (CLI), and automated testing with pytest.

## Features

* View all inventory items
* View a single inventory item
* Add new inventory items
* Update inventory items
* Delete inventory items
* Search products using OpenFoodFacts
* Import products from OpenFoodFacts
* CLI interface
* Automated tests using pytest

## Installation

### Clone Repository

git clone git@github.com:penzimbuthia-sudo/inventory-management.git
cd inventory-management

### Install Dependencies

pipenv install flask requests pytest
pipenv shell


## Running the Flask Application

python app.py

The application runs on:

http://127.0.0.1:5000

## Running the CLI

Open a second terminal:

python cli.py

## Running Tests

python shell
pytest


## API Routes

| Method | Route              | Description                       |
| ------ | ------------------ | --------------------------------- |
| GET    | /                  | Welcome Route                     |
| GET    | /inventory         | Get all inventory items           |
| GET    | /inventory/<id>    | Get a single item                 |
| POST   | /inventory         | Create item                       |
| PATCH  | /inventory/<id>    | Update item                       |
| DELETE | /inventory/<id>    | Delete item                       |
| GET    | /product/<barcode> | Search OpenFoodFacts              |
| POST   | /import/<barcode>  | Import product from OpenFoodFacts |

## Technologies Used

* Python
* Flask
* Requests
* Pytest
* Pipenv
* OpenFoodFacts API
