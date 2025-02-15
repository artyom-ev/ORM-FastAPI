# My FastAPI Project

## Project Structure

app/
├── api/
│   ├── v1/                   # Versioned API endpoints
│   │   ├── endpoints/        # Route handlers
│   │  
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
├── pyproject.toml            # Project dependencies and metadata
├── .env                      # Environment variables
└── streamlit_web_app.py      # Streamlit app
