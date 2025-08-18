import streamlit as st
from modules.resume_parser import extract_text_from_pdf

st.set_page_config(page_title="Upload Resumes", layout="wide")

st.markdown("<h2>📂 Upload Resumes & Job Description</h2>", unsafe_allow_html=True)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please login first.")
else:
    job_description = st.text_area("✍️ Enter the job description")
    uploaded_files = st.file_uploader("Upload candidate resumes (PDF)", type=["pdf"], accept_multiple_files=True)

    if uploaded_files and job_description:
        resumes = [extract_text_from_pdf(file) for file in uploaded_files]
        st.session_state["job_description"] = job_description
        st.session_state["resumes"] = resumes
        st.session_state["resume_names"] = [file.name for file in uploaded_files]
        st.success("✅ Job description & resumes uploaded successfully. Go to Ranking page.")
