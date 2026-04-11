import streamlit as st
import time

# Page loading spinner
with st.spinner("Loading..."):
    time.sleep(2)

# Title
st.title("🔐 Login Page")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = ["Home", "About Us", "Account", "Login", "Contact Us"]
choice = st.sidebar.selectbox("Menu", menu)

# Login Section
if choice == "Login":
    st.subheader("User Login")

    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            if username == "admin" and password == "123456":
                st.success("✅ Login Successful!")
                st.balloons()
            else:
                st.error("❌ Invalid Username or Password")

    with col2:
        if st.button("Cancel"):
            st.warning("⚠️ Login Cancelled")

# Other Pages
elif choice == "Home":
    st.subheader("🏠 Home Page")
    st.write("Welcome to My First Web App!")

elif choice == "About Us":
    st.subheader("ℹ️ About Us")
    st.write("This is a simple Streamlit project.")

elif choice == "Account":
    st.subheader("👤 Account Page")
    st.write("Manage your account here.")

elif choice == "Contact Us":
    st.subheader("📞 Contact Us")
    st.write("Email: example@gmail.com")

# Footer loading
with st.spinner("Please wait..."):
    time.sleep(1)

st.success("Page Loaded Successfully ✅")