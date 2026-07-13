import streamlit as st


def display_tracks(tracks):

    st.divider()

    st.subheader(
        "🎵 Recommended tracks"
    )


    for track in tracks:

        col1, col2 = st.columns([1, 4])


        with col1:
            st.image(
                track["image"],
                width=120
            )


        with col2:

            st.write(
                f"🎧 **{track['name']}**"
            )

            st.write(
                track["artist"]
            )

            st.link_button(
                "Open in Spotify",
                track["spotify_url"]
            )