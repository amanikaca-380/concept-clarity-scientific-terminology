import streamlit as st
import requests

st.title("Sign Up")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

role = st.selectbox(
    "Select your role",
    ["Student", "Professor", "Researcher"]
)

if st.button("Create Account"):
    if not username or not email or not password:
        st.warning("Please fill all fields")

    elif password != confirm_password:
        st.error("Passwords do not match")

    else:
        response = requests.post(
            "http://127.0.0.1:8000/signup",
            json={
                "username": username,
                "email": email,         
                "password": password,
                "role": role.lower()     
            }
        )

        if response.status_code == 200:
            st.success("Account created successfully ")
            st.info("You can now login")

            # Redirect ONLY on success
            st.switch_page("pages/login.py")
        else:
            st.error(response.json().get("detail", "Signup failed"))
