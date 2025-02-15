import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from app.core.config import settings

# Use create_engine for synchronous connections
database_url = (
    f"postgresql+psycopg2://{settings.db_username}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)

engine = create_engine(database_url)

try:
    # Connect to the database
    with engine.connect() as connection:
        # Execute the query
        query = text("SELECT * FROM books;")
        result = connection.execute(query)
        
        # Fetch all rows as dictionaries
        rows = result.mappings().all()
        
        # Convert to a DataFrame
        df = pd.DataFrame(rows)
        
        # Display the DataFrame in Streamlit
        st.subheader('List of my books')
        st.dataframe(df)
except Exception as e:
    # Display any errors in Streamlit
    st.error(f"An error occurred: {e}")
finally:
    # Dispose of the engine to close the connection
    engine.dispose()