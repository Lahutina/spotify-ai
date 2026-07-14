import streamlit as st


def display_album_analysis(album):

    st.divider()

    st.subheader(
        "💿 Album Information"
    )


    st.write(
        f"### {album['album']}"
    )


    st.write(
        f"**Artist:** {album['artist']}"
    )


    st.write(
        "### 📖 History"
    )

    st.info(
        album["summary"]
    )


    st.write(
        "### ✨ Interesting facts"
    )


    for fact in album["interesting_facts"]:

        st.write(
            f"• {fact}"
        )