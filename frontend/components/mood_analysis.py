import streamlit as st


def display_mood_analysis(profile):

    st.subheader("🎭 Your mood")

    st.write(
        profile["explanation"]
    )


    st.write("🎸 Music style")

    for genre in profile["genres"]:
        st.write(
            f"• {genre}"
        )


    st.write("✨ Suggested activities")

    for activity in profile["activities"]:
        st.write(
            f"• {activity}"
        )