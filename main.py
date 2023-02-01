import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Saithulasiram M")
    content = """Hi, I am Saithulasiram Welcome to my website. This page contains python project that I have completed
    and that I am working on. Go on and take a look!!!    
    """
    st.info(content)