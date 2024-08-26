import streamlit as st
import os
from datetime import datetime
from app import run_crew, run_postmortem

st.set_page_config(page_title="SYZYGI AI Analysis", page_icon="🤖", layout="wide")

# Initialize session state
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None
if 'postmortem_complete' not in st.session_state:
    st.session_state.postmortem_complete = False
if 'postmortem_result' not in st.session_state:
    st.session_state.postmortem_result = None

def save_to_file(content, file_type):
    # Create a 'results' directory if it doesn't exist
    if not os.path.exists('results'):
        os.makedirs('results')
    
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create the filename
    filename = f"results/{file_type}_{timestamp}.txt"
    
    # Write the content to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    
    return filename

st.title("SYZYGI AI Analysis")

# Text input for user's custom request
user_request = st.text_area("Enter your request for analysis:", 
                            "Analyze the latest advancements in AI in 2024. Identify key trends, breakthrough technologies, and potential industry impacts.")

if st.button("Run Analysis") or (user_request and not st.session_state.analysis_complete):
    if user_request.strip() == "":
        st.warning("Please enter a request for analysis.")
    else:
        with st.spinner("Running analysis... This may take a few minutes."):
            st.session_state.analysis_result = run_crew(user_request)
        st.session_state.analysis_complete = True

if st.session_state.analysis_complete:
    st.success("Analysis complete!")
    
    st.header("Analysis and Blog Post")
    st.markdown(str(st.session_state.analysis_result))

    # Save analysis results to file
    analysis_file = save_to_file(str(st.session_state.analysis_result), "analysis")
    st.success(f"Analysis results saved to {analysis_file}")

    # New section for postmortem analysis
    st.header("Postmortem Analysis")
    postmortem_request = st.text_area("Enter your request for postmortem analysis:", 
                                      "Conduct a postmortem on the team's performance. How did we do and what could we improve for next time?")

    if st.button("Run Postmortem") or (postmortem_request and not st.session_state.postmortem_complete):
        if postmortem_request.strip() == "":
            st.warning("Please enter a request for postmortem analysis.")
        else:
            with st.spinner("Running postmortem analysis..."):
                st.session_state.postmortem_result = run_postmortem(postmortem_request, str(st.session_state.analysis_result))
            st.session_state.postmortem_complete = True

    if st.session_state.postmortem_complete:
        st.success("Postmortem analysis complete!")
        st.markdown(str(st.session_state.postmortem_result))

        # Save postmortem results to file
        postmortem_file = save_to_file(str(st.session_state.postmortem_result), "postmortem")
        st.success(f"Postmortem results saved to {postmortem_file}")

st.sidebar.header("About")
st.sidebar.info(
    "This app uses CrewAI to analyze topics based on your custom request, generate a blog post about the findings, and conduct a postmortem analysis on the team's performance."
)

# Add a reset button
if st.button("Reset"):
    st.session_state.analysis_complete = False
    st.session_state.analysis_result = None
    st.session_state.postmortem_complete = False
    st.session_state.postmortem_result = None
    st.experimental_rerun()