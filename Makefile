# Target to run the FastAPI application
run:
	uvicorn app.main:app --reload

# Target to run the Streamlit application
streamlit:
	streamlit run streamlit_web_app.py

# # Target to run both FastAPI and Streamlit (optional)
# all: run streamlit

# install:
# 	poetry install

# run:
# 	poetry run uvicorn app.main:app --reload

# test:
# 	poetry run pytest

# docker-build:
# 	docker-compose build

# docker-up:
# 	docker-compose up

# docker-down:
# 	docker-compose down