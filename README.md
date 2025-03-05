# Product Catalog System

## Features

- **Product Search**: Full-text search across product descriptions
- **Multi-filter Capability**:
  - Category filtering (multi-select)
  - Tag filtering (multi-select)
- **Data Seeding**: Built-in command for sample data generation
- **Admin Integration**: Django admin interface for data management

## Get Started

### Installation

```bash
# get repo
git clone https://github.com/Khaki01/product_catalog.git
cd product_catalog

# prepare environment
python3 -m venv venv
. ./venv/bin/activate # MacOS/Linux
venv\Scripts\activate.bat  # Windows

# install packages
pip install -r requirements.txt

```

_python_ for Windows

### Running

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py populate_data # optional
python3 manage.py runserver
```

### Usage

- At <mark>/admin</mark>, you can edit the **Categories**, **Tags**, and **Products**
  - login: admin
  - p: admin
- at main view, you can:
  - search in the bar
  - filter by categories
  - filter by tags

### Attributions
* Data texts(description, name) are generated using ChatGPT
* Initial template style generated with ChatGPT, further edited by myself
