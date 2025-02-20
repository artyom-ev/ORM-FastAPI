import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

db_username = st.secrets["DB_USERNAME"]
db_password = st.secrets["DB_PASSWORD"]
db_host = st.secrets["DB_HOST"]
db_port = st.secrets["DB_PORT"]
db_name = st.secrets["DB_NAME"]

database_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(database_url)

try:
    with engine.connect() as connection:
        query = text("SELECT * FROM climbs;")
        
        result = connection.execute(query)
        rows = result.mappings().all()
        
        df = pd.DataFrame(rows)
        
        st.subheader('List of my climbs')
        st.dataframe(df)
except Exception as e:
    st.error(f"An error occurred: {e}")
finally:
    engine.dispose()