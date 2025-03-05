# Product Catalog System

## Features

- **Product Search**: Full-text search across product descriptions
- **Multi-filter Capability**:
  - Category filtering (multi-select)
  - Tag filtering (multi-select)
- **Data Seeding**: Built-in command for sample data generation
- **Admin Integration**: Django admin interface for data management

## Assumptions
* Each product belongs to a single category
* Each product may have multiple tags
* Selecting multiple categories will filter if product matches one of them
* Selecting multiple tags will filter if product matches at least one of them
* Search bar use only product descriptions (not names or other fields)
* Filtering using search, category, and tag will filter in combination (AND). 
* Use basic `icontains` query rather than full-text search engine
* No pagination implemented for product results (only 25 items)


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
  - Run `python manage.py createsuperuser` to access admin
- at main view, you can:
  - search in the bar
  - filter by categories
  - filter by tags

### Attributions
* Data texts(description, name) are generated using ChatGPT
* Initial template style generated with ChatGPT, further edited by myself
