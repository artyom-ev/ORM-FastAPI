# Target to run the FastAPI application
run:
	uvicorn main:app --reload

# Target to run the Streamlit application
streamlit:
	streamlit run /Users/artem/Documents/climbing-progress/app.py

# Target to run both FastAPI and Streamlit (optional)
all: run streamlit