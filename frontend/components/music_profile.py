import streamlit as st


def display_music_profile(profile):

    st.subheader("🎵 Your Music Profile")


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Mood",
            profile["mood"]
        )


    with col2:

        st.metric(
            "Energy",
            profile["energy"]
        )


    st.write("### 🎸 Genres")

    for genre in profile["genres"]:
        st.write(
            f"• {genre}"
        )


    st.write("### 🎯 Activities")

    for activity in profile["activities"]:
        st.write(
            f"• {activity}"
        )


    st.write("### 💭 AI Explanation")

    st.info(
        profile["explanation"]
    )