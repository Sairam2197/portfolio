import streamlit as st

st.header("Contact Me/Leave a Feedback")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your Message here")
    button = st.form_submit_button()
    if button:
        message = message + user_email
        print("Thanks for your Response")
        st.balloons()

