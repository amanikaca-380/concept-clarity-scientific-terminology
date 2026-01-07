import streamlit as st
import requests

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email and password:
        response = requests.post(
            "http://127.0.0.1:8000/login",
            json={
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:
            data = response.json()
            st.session_state["token"] = data["access_token"]
            st.session_state["username"] = data["username"]
            st.session_state["logged_in"] = True
            st.success(f"Welcome {data['username']} ")
            st.session_state["logged_in"] = True
            st.session_state["username"] = data["username"]
        else:
            st.error(response.json()["detail"])
    else:
        st.warning("Please enter email and password")
    st.switch_page("pages/home.py")
