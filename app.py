import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Retrieve database credentials from Streamlit secrets
db_username = st.secrets["DB_USERNAME"]
db_password = st.secrets["DB_PASSWORD"]
db_host = st.secrets["DB_HOST"]
db_port = st.secrets["DB_PORT"]
db_name = st.secrets["DB_NAME"]

# Construct the database URL
database_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create the SQLAlchemy engine
engine = create_engine(database_url)

# Use a context manager to handle the connection
try:
    with engine.connect() as connection:
        # Wrap the SQL query in SQLAlchemy's `text()` function
        query = text("SELECT * FROM climbs;")
        
        # Execute the query and fetch results as a list of dictionaries
        result = connection.execute(query)
        rows = result.mappings().all()
        
        # Convert the result to a DataFrame
        df = pd.DataFrame(rows)
        
        # Display the DataFrame in Streamlit
        st.subheader('List of my climbs')
        st.dataframe(df)
except Exception as e:
    st.error(f"An error occurred: {e}")
finally:
    # Ensure the engine is disposed of properly
    engine.dispose()