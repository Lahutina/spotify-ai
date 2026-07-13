import streamlit as st

from services.backend_client import analyze_mood, get_recommendations
from components.mood_analysis import display_mood_analysis
from components.tracks import display_tracks
from components.sidebar import render_sidebar


st.set_page_config(page_title="Spotify AI", page_icon="🎵", layout="centered")


render_sidebar()


st.title("🎵 Spotify AI Assistant")


st.write(
    """
    Describe your mood and AI will create
    a personalized music experience.
    """
)


tab1, tab2, tab3 = st.tabs(["🎭 Mood", "📷 Photo", "💿 Album Cover"])


with tab1:
    text = st.text_area("How are you feeling?")

    if st.button("Generate Recommendations"):
        if text:
            with st.spinner("Understanding your mood..."):
                profile = analyze_mood(text)

            display_mood_analysis(profile)

            with st.spinner("Finding music for you..."):
                recommendation = get_recommendations(profile)

            display_tracks(recommendation["tracks"])
