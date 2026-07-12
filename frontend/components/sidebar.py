import streamlit as st


def render_sidebar():

    st.sidebar.title(
        "🎧 Spotify AI"
    )


    st.sidebar.write(
        """
        AI-powered music assistant.

        Current features:
        
        ✅ Mood analysis
        
        🔜 Photo → Music
        
        🔜 Album Cover Analysis
        """
    )