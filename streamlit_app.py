import streamlit as st
from app import run_crew

st.set_page_config(page_title="AI Advancements Analysis", page_icon="🤖", layout="wide")

st.title("AI Advancements Analysis")

if st.button("Run Analysis"):
    with st.spinner("Running analysis... This may take a few minutes."):
        result = run_crew()
    
    st.success("Analysis complete!")
    
    st.header("Analysis and Blog Post")
    st.markdown(str(result))

st.sidebar.header("About")
st.sidebar.info(
    "This app uses CrewAI to analyze the latest advancements in AI and generate a blog post about the findings."
)