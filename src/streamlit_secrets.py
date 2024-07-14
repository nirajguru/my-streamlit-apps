import streamlit as st
# Secrets should be read from community cloud

# Secrets can also be stored locally here in .streamlit/secrets.toml
st.title("Storing secrets")
st.write(st.secrets["message"]) 