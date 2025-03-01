run-back:
	cd backend && uvicorn main:app --reload

run-front:
	streamlit run frontend/streamlit_web.py

run:
	cd backend && uvicorn main:app --reload & \
	streamlit run frontend/streamlit_web.py

stop:
	pkill -f "uvicorn main:app"
	pkill -f "streamlit run frontend/streamlit_web.py"