import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", caption='Thinking whether to use for loop or while loop in my next program', width=500)

with col2:
    st.title("Saithulasiram M")
    content = """Hi, I am Saithulasiram Welcome to my website. I am working as a System Admin in Kyndryl I have been
    practising Python from Udemy for quite a while now. I like coding but the :red[most fun] part is when an issue comes
    with my code, I like investigating and solving the error on my own :sunglasses:.
         
    """
    st.info(content)


st.text("""
This page contains python project that I have completed and that I am working on. Go on and take a look!!!
""")

