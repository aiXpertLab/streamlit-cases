import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

@st.cache_data
def data_upload():
    df =pd.read_csv('pages/data/food.csv')
    return df

df = data_upload()

# Using streamlit.write(dataframe)
st.write("Using streamlit.write(dataframe):")
st.write(df)

# Using st.dataframe(dataframe)
st.write("Using st.dataframe(dataframe):")
st.dataframe(df)
st.info(len(df))

# Using st.table(dataframe)
st.write("Using st.table(dataframe):")
st.table(df.head(5))
st.divider()

# st.markdown("#### Using AgGrid:")
AgGrid(df)

