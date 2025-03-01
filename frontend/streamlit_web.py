import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from src.config import settings

database_url = settings.DATABASE_URL_psycopg

engine = create_engine(database_url)

try:
    with engine.connect() as connection:
        query = text("SELECT * FROM books;")
        
        result = connection.execute(query)
        rows = result.mappings().all()
        
        df = pd.DataFrame(rows)
        
        st.subheader('List of my books')
        st.dataframe(df)
except Exception as e:
    st.error(f"An error occurred: {e}")
finally:
    engine.dispose()