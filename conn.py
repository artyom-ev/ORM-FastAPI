import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text  # Import the `text` function

# Load environment variables from .env file
load_dotenv()

# Retrieve database credentials from environment variables
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Construct the database URL
database_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create the SQLAlchemy engine
engine = create_engine(database_url)

# Connect to the database and execute the query
try:
    connection = engine.connect()
    
    # Wrap the SQL query in SQLAlchemy's `text()` function
    query = text("SELECT * FROM climbs;")
    
    # Execute the query
    result = connection.execute(query)
    
    # Print each row
    for row in result:
        print(row)
finally:
    # Close the connection
    connection.close()