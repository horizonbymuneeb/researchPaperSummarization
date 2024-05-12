import streamlit as st
from transformers import pipeline

# Initialize the summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Title for the app
st.title('Text Summarization App')

# Text input box for the article
article = st.text_area('Enter the article to summarize:', height=200)

# Button to summarize the text
if st.button('Summarize'):
    # Check if the article is not empty
    if article:
        # Summarize the article
        summary = summarizer(article, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        # Display the summarized text
        st.write(summary)
    else:
        st.warning('Please enter some text to summarize.')
