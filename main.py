import streamlit as st
import time
#st.markdown("""<style>*{background-color:white;}</style>""",unsafe_allow_html=True)
with st.spinner("Loading...."):
    time.sleep(5)

st.title("My First web page on GitHub!!!")
    
st.balloons()
with st.sidebar:
    st.success("Home")
    st.success("About Us")
    st.success("Account")
    st.success("Login")
        
    with st.spinner("Loading ....."):
        time.sleep(5)
    st.success("Done")

