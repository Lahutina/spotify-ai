import streamlit as st

from services.backend_client import analyze_mood
from components.music_profile import display_music_profile
from components.sidebar import render_sidebar


st.set_page_config(
    page_title="Spotify AI",
    page_icon="🎵",
    layout="centered"
)


render_sidebar()


st.title(
    "🎵 Spotify AI Assistant"
)


st.write(
    """
    Describe your mood and AI will create
    a personalized music profile.
    """
)


tab1, tab2, tab3 = st.tabs(
    [
        "🎭 Mood",
        "📷 Photo",
        "💿 Album Cover"
    ]
)


with tab1:

    text = st.text_area(
        "How are you feeling?"
    )


    if st.button(
        "Analyze Mood"
    ):

        if text:

            with st.spinner(
                "AI is thinking..."
            ):

                profile = analyze_mood(text)

            display_music_profile(
                profile
            )


with tab2:

    st.header(
        "📷 Photo → Music"
    )

    st.info(
        "Vision AI will be added here."
    )


with tab3:

    st.header(
        "💿 Album Cover Analysis"
    )

    st.info(
        "Vision + RAG will be added here."
    )