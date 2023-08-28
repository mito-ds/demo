#
import os
import random

os.environ['MITO_CONFIG_VERSION'] = '2'
os.environ['MITO_CONFIG_FEATURE_DISPLAY_AI_TRANSFORMATION'] = 'True'

import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

st.set_page_config(layout="wide")
st.title("Mito Spreadsheet Demo")

def between_sections():
    st.markdown("#")
    st.markdown("#")
    st.markdown("---")
    st.markdown("#")
    st.markdown("#")

st.subheader("Transition a spreadsheet process to Python")
new_dfs, code = spreadsheet(import_folder='.', key='spreadsheet transition')
st.write(new_dfs)
st.code(code)

# A button that allows the user to save the code to a file
if st.button("Save Code"):
    with open("output.py", "w") as f:
        f.write(code)
    st.success("Saved to output.py")

between_sections()

st.subheader("Using a Mito spreadsheet to access data")

_, code = spreadsheet(key='data import')
st.code(code)

between_sections()

st.subheader("Custom Importers")

st.code("""
def get_customers(location: str, limit: int):
    # Import SQL libraries
    import sqlite3
    import pandas as pd
    
    # Connect to a database
    conm = sqlite3.connect('Customers.db')
    
    # Read data from SQL to pandas dataframe
    data = pd.read_sql_query(f'Select * from CUSTOMERS LIMIT {limit};', con)
    
    return data
""")
        
def get_customers(location: str, limit: int):
    import pandas as pd

    CUSTOMER_NAMES = [
        'John Smith', 'Jane Doe', 'Ben Doe', 'Sally Smith', 'Harry Potter', 'Ron Weasley', 'Hermione Granger',
        'Albus Dumbledore', 'Severus Snape', 'Rubeus Hagrid', 'Draco Malfoy', 'Neville Longbottom', 'Luna Lovegood',
        'Ginny Weasley', 'Fred Weasley', 'George Weasley', 'Voldemort', 'Sirius Black', 'Remus Lupin', 'Peter Pettigrew',
        'James Potter', 'Lily Potter', 'Dobby', 'Lucius Malfoy', 'Bellatrix Lestrange', 'Cho Chang', 'Cedric Diggory',
        'Fleur Delacour', 'Viktor Krum', 'Dudley Dursley', 'Petunia Dursley', 'Vernon Dursley', 'Dolores Umbridge',
        'Arthur Weasley', 'Molly Weasley', 'Narcissa Malfoy', 'Kingsley Shacklebolt', 'Percy Weasley', 'Bill Weasley',
    ]


    # Random data. Should be limit number of rows, and all be from location. Should be random customer names
    df = pd.DataFrame({
        'location': [location] * limit,
        'customer_name': CUSTOMER_NAMES[:limit],
        'customer_id': [i for i in range(limit)],
        'customer_age': [random.random() * 100 for _ in range(limit)]
    })

    return df


_, code = spreadsheet(import_folder='.', key='custom importer', importers=[get_customers])
st.code(code)

between_sections()

st.subheader("Custom sheet functions")

st.code("""
def GET_DEFAULT_RISK(x):
    # Connect to internal risk model
    model = RiskModel()
    
    # Run risk model on each row
    return x.apply(lambda _: model.predict(_))      
""")

def GET_DEFAULT_RISK(x):
    import random
    return x.apply(lambda _: random.random())

_, code = spreadsheet(import_folder='.', sheet_functions=[GET_DEFAULT_RISK], key='sheet function')
st.code(code)


# TODO: I should show the full automation process
