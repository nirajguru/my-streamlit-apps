import streamlit as st
import pandas as pd

st.title("Streamlit file uploader")

st.subheader("Input CSV")
uploaded_csv = st.file_uploader("Choose a CSV file", 
                                accept_multiple_files=False)
if uploaded_csv is not None:
    df = pd.read_csv(uploaded_csv)
    st.write(df)
    st.download_button(
        label="Download data as CSV",
        data=df.to_csv(),
        file_name='large_df.csv',
        mime='text/csv',
    )
