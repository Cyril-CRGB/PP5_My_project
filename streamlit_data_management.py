import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import psycopg2 # import the PostgresQL connector
#import env




# Connect to your database
#@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def connect_to_db():
    DATABASE_URL = os.environ.get('DATABASE_URL') # Fetch the DATABASE_URL from environnement variables
    if DATABASE_URL is None:
        st.error('DATABASE_URL is not set.')
        return None
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require') # Connect to the database
        return conn
    except Exception as e:
        st.error(f"Connection to databased failed: {e}")
        return None


#@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_original_data():
    conn = connect_to_db()
    if conn is None:
        return pd.DataFrame() # Return empty DataFrame if connection fails
    query = "SELECT * FROM crime_data_from_2020_to_present LIMIT 10000;" # Update table
    dforigine = pd.read_sql(query, conn) # fetch data from the database
    conn.close() # Close the connection
    return dforigine

#@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_crime_committed_analyses():
    conn = connect_to_db()
    if conn is None:
        return pd.DataFrame() # Return empty DataFrame if connection fails
    query = "SELECT * FROM crime_description_table;" # Update table
    dfcca = pd.read_sql(query, conn) # change the delimiter if needed
    conn.close()
    return dfcca

#@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_cleaned_data_short():
    conn = connect_to_db()
    if conn is None:
        return pd.DataFrame() # Return empty DataFrame if connection fails
    query = "SELECT * FROM dataPP5_cleaned_10k;" # Update table
    dfcleanedshort = pd.read_sql(query, conn)
    conn.close()
    return dfcleanedshort

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)