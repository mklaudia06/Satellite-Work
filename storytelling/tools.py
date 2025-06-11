import streamlit as st 

def for_titles_centered (text, level="h1", color="blue"):
    st.markdown(
        f"<{level} style='text-align: center; color: {color};'>{text}</{level}>",
        unsafe_allow_html=True
    )


