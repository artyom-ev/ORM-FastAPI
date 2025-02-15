# ORM-FastAPI App

## Key Features of Structure

- The `api/` directory contains versioned endpoints, making it easy to add new versions in the future.
- The `db/` directory separates database models, repositories, and session management.
- **`schemas/`**: Handles request/response validation with Pydantic.
- **`core/`**: Centralizes configuration and other core functionality.
- **`repositories/`**: Abstracts database operations, making the code more testable and maintainable.
- The structure is scalable. You can easily add new models, endpoints, or services without disrupting existing code.
- **`docker-compose.yml`**: Simplifies local development with Docker.
- **`Makefile`**: Automates common tasks like running tests or starting the app.
- **`pyproject.toml`**: Manages dependencies and project metadata.

---

## Structure

```sh
app/
├── api/
│   ├── v1/                   # Versioned API endpoints
│   │   ├── endpoints/        # Route handlers
│   │   │   ├── books.py      # Book-related routes
│   │   │   └── setup.py      # Database setup route
│   │   └── routers.py        # Aggregates all routes for v1
├── core/
│   ├── config.py             # Configuration settings
├── db/
│   ├── base.py               # Base ORM model
│   ├── models/               # Database models
│   │   └── book.py           # Book model
│   ├── repositories/         # Repository layer
│   │   └── book.py           # Book repository
│   └── session.py            # Database session management
├── schemas/                  # Pydantic schemas
│   └── book.py               # Book schemas
├── main.py                   # FastAPI app initialization
├── docker-compose.yml        # Docker Compose for local development
├── Makefile                  # Make commands for common tasks
├── README.md                 # Project documentation
├── uv.toml            # Project dependencies and metadata
├── .env                      # Environment variables
└── streamlit_web_app.py      # Streamlit app
```
