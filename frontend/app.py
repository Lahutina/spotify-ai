import streamlit as st
import requests


st.title("🎵 Spotify-AI")

st.write(
    "Your AI-powered music companion"
)


if st.button("Check backend"):

    response = requests.get(
        "http://127.0.0.1:8000/"
    )

    st.success(response.json()["message"])