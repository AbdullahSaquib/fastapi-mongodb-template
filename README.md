# FastAPI with MongoDB

This project demonstrates how to set up a FastAPI application with MongoDB using Motor for asynchronous database operations.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AbdullahSaquib/fastapi-mongodb-template
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file based on template.env file, and add your MongoDB credentials:

5. Running the Application
Start the FastAPI application:
```bash
uvicorn app.main:app --reload
```

The application will be available at http://127.0.0.1:8000/docs.

## API Endpoints

### Create Item
  POST /items/

### Read Item
  GET /items/{item_id}

### Update Item
  PUT /items/{item_id}

### Delete Item
  DELETE /items/{item_id}

### Read Items
  GET /items/

### Aggregate Items
  GET /items/aggregate/
