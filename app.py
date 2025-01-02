import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd

conn = st.connection('supabase', type=SupabaseConnection)

response = conn.table("climbs").select("*").execute()

df = pd.DataFrame(response.data)

st.subheader('List of my climbs')

st.dataframe(df)