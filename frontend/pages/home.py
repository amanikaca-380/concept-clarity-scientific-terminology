import streamlit as st
import requests

st.title(" Scientific Term Explainer")


if "username" in st.session_state:
    st.write(f"Hello {st.session_state['username']} !")
else:
    st.info("You are searching as an anonymous user")

#  Search input
term = st.text_input("Enter a scientific term")

if st.button("Search"):
    if term.strip() == "":
        st.warning("Please enter a term")
    else:
        headers = {}

        #  Send token ONLY if logged in
        if "token" in st.session_state:
            headers["Authorization"] = f"Bearer {st.session_state['token']}"

        response = requests.post(
            "http://127.0.0.1:8000/search",
            json={"term": term},
            headers=headers
        )

        if response.status_code == 200:
            st.success("Search completed ")
            st.info(f"You searched: {term}")
            st.write("AI explanation will appear here")
        else:
            st.error("Something went wrong. Please try again.")

st.divider()

#  Logout button ONLY for logged-in users
if "token" in st.session_state:
    if st.button("Logout"):
        st.session_state.clear()
        st.success("Logged out successfully")
        st.stop()
