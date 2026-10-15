import streamlit as st
from summarizer import summarize

st.title("Text Summarizer")
text = st.text_area("Paste your text here")

sentences = st.sidebar.slider("Number of sentences", 1, 10, 3)

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please paste some text first.")
    else:
        try:
            st.write(summarize(text, sentences))
        except Exception as e:
            st.error(f"Something went wrong: {e}")